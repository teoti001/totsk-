## Prebattle Orders & Deployment by Caba'drin
## v0.95.7
## 31 Jan 2012

from module_constants import *

## Prebattle Orders & Deployment Begin
#PBOD General
skirmish_min_distance = 1500 #Min distance you wish maintained, in cm. Where agent will retreat
skirmish_max_distance = 2500 #Max distance to maintain, in cm. Where agent will stop retreating

order_frame_presobj = "trp_bandit_leaders_end"  #dummy troop slots used in battle Floris: "trp_tpe_presobj"   Native: "trp_bandit_leaders_end"
slot_party_pbod_mod_version = 46  #slot_village_player_can_not_steal_cattle
current_version = 957

#Deployment
slot_troop_prebattle_first_round           = 37  #slot_lady_no_messages 
#slot_troop_prebattle_array                 = 38  #slot_lady_last_suitor 
#slot_troop_prebattle_preupgrade_check      = 39  #slot_troop_betrothal_time
slot_troop_prebattle_stack_number          = 51  #slot_troop_intrigue_impatience
slot_troop_prebattle_stack_xp              = 52  #slot_lord_reputation_type 
slot_party_prebattle_customized_deployment = 47  #slot_center_accumulated_rents  
#slot_party_prebattle_battle_size           = 48  #slot_center_accumulated_tariffs 
#slot_party_prebattle_size_in_battle        = 49  #slot_town_wealth  
#slot_party_prebattle_in_battle_count       = 50  #slot_town_prosperity
#Split Divisions
slot_party_prebattle_customized_divisions  = 51  #slot_town_player_odds 
slot_party_reinforcement_stage 		       = 107 #for main_party_backup
slot_troop_prebattle_alt_division          = 48  #slot_troop_set_decision_seed
slot_troop_prebattle_alt_division_percent  = 49  #slot_troop_temp_decision_seed 
slot_troop_prebattle_alt_division_amount   = 50  #slot_troop_recruitment_random 
#Troop slots--for soldiers (non-heros, non-lords, non-player) only
#Party slots--for the main party and main party backup only
#Orders
slot_party_prebattle_plan                  = 231 #slot_center_shipyards
slot_party_prebattle_num_orders            = 232 #slot_center_household_gardens 
slot_party_prebattle_order_array_begin     = 250 #slot_town_trade_good_prices_begin 
#Party slots--for the main party only--up to 320 used in this version
#reg()s from 6-50 used in this version (only during order presentation)
#Weather Prof Decrease - temp, used only for 1 mission at a time then can be discarded
slot_troop_proficiency_modified  = 335
slot_troop_orig_wpt_archery      = 336
slot_troop_orig_wpt_crossbow     = 337
slot_troop_orig_wpt_throwing     = 338
slot_troop_pnty_wpt_archery      = 339 ##heroes only
slot_troop_pnty_wpt_crossbow     = 340 ##heroes only
slot_troop_pnty_wpt_throwing     = 341 ##heroes only
#Agent Slots
slot_agent_lance         = 33
slot_agent_horsebow      = 34
slot_agent_spear         = 35
slot_agent_horse         = 36
slot_agent_volley_fire   = 37
slot_agent_spearwall     = 38
slot_agent_player_braced = 39
slot_agent_alt_div_check = 40
#slot_agent_new_division  = 41
#Team Slots (so high to allow for formations)
slot_team_d0_order_weapon     = 300 #plus 8 more for the other divisions
slot_team_d0_order_shield     = 309 #plus 8 more for the other divisions
slot_team_d0_order_skirmish   = 318 #plus 8 more for the other divisions
slot_team_d0_order_volley     = 327 #plus 8 more for the other divisions
slot_team_d0_order_sp_brace   = 336 #plus 8 more for the other divisions

slot_team_d0_formation_to_resume = 350

#PBOD Preference Slots (used for p_main_party; available 72 - 108)
slot_party_pref_prefs_set    = 72
slot_party_pref_div_dehorse  = slot_town_village_product         #76
slot_party_pref_div_no_ammo  = slot_town_rebellion_readiness     #77
slot_party_pref_wu_lance     = slot_town_arena_melee_mission_tpl #78
slot_party_pref_wu_harcher   = slot_town_arena_torny_mission_tpl #79
slot_party_pref_wu_spear     = slot_town_arena_melee_1_num_teams #80
slot_party_pref_dmg_tweaks   = slot_town_arena_melee_1_team_size #81
slot_party_pref_spear_brace  = slot_town_arena_melee_2_num_teams #82
slot_party_pref_formations   = slot_town_arena_melee_2_team_size #83
slot_party_pref_bodyguard    = slot_town_arena_melee_3_num_teams #84
slot_party_pref_bc_continue  = slot_town_arena_melee_3_team_size #85
slot_party_pref_bc_charge_ko = slot_town_arena_melee_cur_tier    #86
slot_party_pref_wp_prof_decrease = 87
slot_party_pref_real_deployment  = 88

slot_party_temp_cheatmode  = 72 #for party 2

#Order Tracking
slot_party_gk_order          = 108
slot_party_gk_order_hold_over_there = slot_party_gk_order #for party #2 at the moment, also used for backup_party

#Order Constants
ranged    = 0
onehand   = 1
twohands  = 2
polearm   = 3
shield    = 4
noshield  = 5
free      = 6 #shield
clear     = -1
begin     = 1
end       = 0

cam_mode_default = 0
cam_mode_follow  = 1
cam_mode_free    = 2
cam_mode_shoot   = 3
cam_position     = 47 #pos47


BP_Spawn = 0




#Values for agent_get_combat_state
cs_free                      = 0
cs_target_in_sight           = 1     # ranged units
cs_guard                     = 2     # no shield
cs_wield                     = 3     # reach out weapon, preparing to strike, melee units
cs_fire                      = 3     # ranged units
cs_swing                     = 4     # cut / thrust, melee units
cs_load                      = 4     # crossbow units
cs_still                     = 7     # melee units, happens, not always (seems to have something to do with the part of body hit), when hit
cs_no_visible_targets        = 7     # ranged units or blocking iwth a shield
cs_target_on_right_hand_side = 8     # horse archers

# For the player or dead units it always returns 0.
# But for living human agents here are some of the values it can return and what each seems to mean:
# 0 = nothing active
# 1 = firing ranged
# 3 = preparing and holding attack (either melee or ranged)
# 4 = swinging with melee
# 7 = recovering from being hit
# 8 = ranged equipped, no target in field of view

#Key definitions moved to globals to allow for in-game remapping
#See script "prebattle_init_default_keys" and the presentation "pbod_redefine_keys"

#AutoLoot compile-time-set item slots no longer necessary with WSE

#-- Dunde's Key Config BEGIN
from header_triggers import *
#-- Parts to modify as your mod need --------------
keys_list = [
			  ("$key_camera_forward",  key_up,                "Camera Forward"),
              ("$key_camera_backward", key_down,              "Camera Backward"),
	          ("$key_camera_left",     key_left,              "Camera Turn Left"),
	          ("$key_camera_right",    key_right,             "Camera Turn Right"),
			  ("$key_camera_zoom_plus",key_numpad_plus,       "Camera Up"),
              ("$key_camera_zoom_min", key_numpad_minus,      "Camera Down"),
			  ("$key_camera_next",     key_left_mouse_button, "Next BOT"),
              ("$key_camera_prev",     key_right_mouse_button,"Prev BOT"),
			  ("$key_camera_toggle",   key_end,               "Toggle Camera Mode"),
	          ("$key_order_7",         key_f7,                "Select Order 7"),
	          ("$key_order_8",         key_f8,                "Select Order 8"),
	          ("$key_order_9",         key_f9,                "Select Order 9"),
			  ("$key_order_10",        key_f10,               "Select Order 10"),
	          ("$key_special_0",       key_b,                 "Spear Brace"),
	          ("$key_special_1",       key_m,                 "Call Horse"),
			  #("$key_special_2",       key_g,                 "Deploy Pavise"), #Floris Only
			  ("$key_special_3",       key_left_mouse_button, "Shield Bash Attack"),	  
            ] # end of keys_list
#--------------------------------------------------
all_keys_list   = [
(key_1, "1"), (key_2, "2"), (key_3, "3"), (key_4, "4"), (key_5, "5"), (key_6, "6"), (key_7, "7"), (key_8, "8"), (key_9, "9"), (key_0, "0"), 
(key_a, "A"), (key_b, "B"), (key_c, "C"), (key_d, "D"), (key_e, "E"), (key_f, "F"), (key_g, "G"), (key_h, "H"), (key_i, "I"), (key_j, "J"),
(key_k, "K"), (key_l, "L"), (key_m, "M"), (key_n, "N"), (key_o, "O"), (key_p, "P"), (key_q, "Q"), (key_r, "R"), (key_s, "S"), (key_t, "T"), 
(key_u, "U"), (key_v, "V"), (key_w, "W"), (key_x, "X"), (key_y, "Y"), (key_z, "Z"), 
(key_numpad_0, "Numpad 0"), (key_numpad_1, "Numpad 1"), (key_numpad_2, "Numpad 2"), (key_numpad_3, "Numpad 3"), (key_numpad_4, "Numpad 4"), 
(key_numpad_5, "Numpad 5"), (key_numpad_6, "Numpad 6"), (key_numpad_7, "Numpad 7"), (key_numpad_8, "Numpad 8"), (key_numpad_9, "Numpad 9"), 
(key_num_lock, "Num Lock"), (key_numpad_slash, "Numpad DIV"), (key_numpad_multiply, "Numpad MUL"), 
(key_numpad_minus, "Numpad MIN"), (key_numpad_plus, "Numpad PLUS"), (key_numpad_enter, "Numpad ENTER"), (key_numpad_period, "Numpad DEL)"), 
(key_insert, "Insert"), (key_delete, "Delete"), (key_home, "Home"), (key_end, "End"), (key_page_up, "Page Up"), (key_page_down, "Page Down"), 
(key_up, "Up"), (key_down, "Down"), (key_left, "Left"), (key_right, "Right"),
(key_f1, "F1"), (key_f1, "F2"), (key_f3, "F3"), (key_f4, "F4"),  (key_f5, "F5"),  (key_f6, "F6"), 
(key_f7, "F7"), (key_f8, "F8"), (key_f9, "F9"), (key_f10, "F10"), (key_f11, "F11"), (key_f12, "F12"),
(key_space, "Space Bar"), (key_enter, "Enter"), (key_tab, "Tab"), (key_back_space, "Backspace"), 
(key_open_braces, "[ "), (key_close_braces, " ] "), (key_comma, " < "), (key_period, " > "), (key_slash, " ? "), (key_back_slash, "\\"), 
(key_equals, " = "), (key_minus, " -- "), (key_semicolon, "Semicolon"), (key_apostrophe, "Apostrophe"), (key_tilde, "Tilde"), (key_caps_lock, "Caps Lock"),
(key_left_shift, "Left Shift"), (key_right_shift, "Right Shift"), (key_left_control, "Left Ctrl"), (key_right_control, "Right Ctrl"), (key_left_alt, "Left Alt"), (key_right_alt, "Right Alt"),
(key_left_mouse_button, "Left Click"), (key_right_mouse_button, "Right Click"), (key_middle_mouse_button, "Middle Mouse Button"), 
(key_mouse_button_4, "Mouse Button 4"), (key_mouse_button_5, "Mouse Button 5"), (key_mouse_button_6, "Mouse Button 6"), 
(key_mouse_button_7, "Mouse Button 7"), (key_mouse_button_8, "Mouse Button 8"), (key_mouse_scroll_up, "Mouse Scroll Up"), (key_mouse_scroll_down, "Mouse Scroll Down"), ]

number_of_keys            = len(keys_list)
number_of_all_keys        = len(all_keys_list)
two_columns_limit         = 20 

slot_default_keys_begin   = 0
slot_keys_begin           = slot_default_keys_begin + number_of_keys
slot_key_overlay_begin    = slot_keys_begin         + number_of_keys
slot_key_defs_begin       = slot_key_overlay_begin  + number_of_keys + number_of_keys

key_config_data = "trp_temp_array_c" #"trp_key_config"
key_names_begin = "str_key_no1"
key_label_begin = "str_key_1"
#-- Dunde's Key Config END

## Prebattle Orders & Deployment End