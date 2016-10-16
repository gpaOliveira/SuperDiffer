from SuperDiffer.id.models import ID
from SuperDiffer import db
import pdb

def count():
    """Helper testing function to count all IDs"""
    return len(ID.query.all())
    
def list():
    """Helper testing function to list all IDs"""
    data = ID.query.all()
    to_return = []
    for d in data:
        entry = {}
        entry["id"] = d.id
        entry["description"] = d.description.encode('utf-8','ignore')
        entry["data"] = d.data.encode('utf-8','ignore')
        to_return.append(entry)
    return to_return
    
def add(id, descriptor, data):
    """Add a description and a data to our model - rollback and return False if anything goes wrong (PK not respected, for example)"""
    try:
        u = ID(id = id, description = descriptor, data = data)
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return False
    return True

def _grab_descriptors_values_to_diff(id_to_diff, descriptors_to_diff):
    """"Grab all the descriptors values to diff or get out"""
    to_diff = {}
    for d in descriptors_to_diff:
        value = ID.query.filter_by(id = id_to_diff, description = d).first()
        if value:
            to_diff[d] = value.data
        else:
            return None
    return to_diff
    
def _grab_pairs_keys_to_compare(descriptors_list_to_diff):
    """"Grab all pair of keys to compare.
    Knowing that we already have an array containing the keys to be compared, we iterate on its indexes twice in order to just grab pairs of them. We doesn't want equal pairs indexes to be compared, and also (1,2) is the same as (2,1) for us."""
    pairs_to_diff = [ ( descriptors_list_to_diff[i],
                        descriptors_list_to_diff[j])
                      for i in range(len(descriptors_list_to_diff))
                      for j in range(len(descriptors_list_to_diff))
                      if i < j
                    ]
    return pairs_to_diff
    
def _diff_values(value_one, value_two):
    """Compute insights on where the diffs are and their lenght on strings with the same size (without using https://docs.python.org/2/library/difflib.html)"""
    
    #initialize returned struct
    diff_data = {"size":"equal", "diffs":[]}
    
    #we won't compare different size strings
    if len(value_one) != len(value_two):
        diff_data["size"] = "not equal"
        return diff_data
    
    #find the diff indexes, as follows:
    #(a) on the first different char in a sequence, save that index on a buffer along with the sequence lenght (only 1 for now)
    #(b) on the successive different chars in a sequence, increment the lenght of the sequence on the buffer
    #(c) on the first equal char after a sequence of differences, add the buffer to our list and reset it if needed
    current_diff = None
    for char_index in range(len(value_one)):
        if value_one[char_index] != value_two[char_index]:
            if not current_diff: # (a) situation, as above
                current_diff = {"diff_start":char_index, "chain":1}
            else: # (b) situation, as above
                current_diff["chain"] += 1
        else:
            if current_diff: # (c) situation, as above
                diff_data["diffs"].append(current_diff)
                current_diff = None
    
    #let's not forget to append anything that has remained on the buffer
    if current_diff:
        diff_data["diffs"].append(current_diff)
        current_diff = None
    
    return diff_data
    
def diff(id_to_diff, descriptors_to_diff):
    to_diff = _grab_descriptors_values_to_diff(id_to_diff, descriptors_to_diff)
    if not to_diff:
        return None
    
    pair_keys_to_diff = _grab_pairs_keys_to_compare(descriptors_to_diff)
    if len(pair_keys_to_diff) == 0:
        return None
    
    diffs = {}
    for key_one, key_two in pair_keys_to_diff:
        diff_key = "{0}_{1}".format(key_one, key_two)
        diffs[diff_key] = _diff_values(
                            to_diff[key_one],
                            to_diff[key_two]
                        )
    return diffs