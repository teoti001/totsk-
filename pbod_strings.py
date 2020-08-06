## Prebattle Orders & Deployment by Caba'drin
## v0.95.7
## 31 Jan 2012

#-- Dunde's Key Config BEGIN
from module_constants import keys_list, all_keys_list
def get_key_strings():
   key_strings = []
   for i_key in xrange(len(all_keys_list)):
       key_strings.append(("key_"+str(i_key+1), all_keys_list[i_key][1]))    
   for i_key in xrange(len(keys_list)):
       key_strings.append(("key_no"+str(i_key+1), keys_list[i_key][2]))      
   return key_strings[:]  
#-- Dunde's Key Config END

strings = [
##PBOD
("real_deployment_start", "Place your troops before the battle starts by first selecting a division, then holding down '{s48}' and releasing the flag where you want the division. If you want the divison to begin in formation, first give the formation order, then place them with '{s48}'.^^Your Tactics Skill allows you {reg0} placements.^Hit '{s49}' to start the battle before they are all used."),
("real_deployment_end",   "Deployment Complete^^Prepare for battle!"),
("real_deployment_inprogress", "{!}{reg0} placement{reg1?s:} with '{s48}' remaining or hit '{s49}' to start the battle now."),
##PBOD
] + get_key_strings()

from util_common import add_objects

# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "strings"
        orig_strings = var_set[var_name_1]
        add_objects(orig_strings, strings)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)