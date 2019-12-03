#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
From the paper Identifying Financial Reporting Quality from Grammatical Errors in Financial Statements§
@authors: Jacquelyn Gillette and Gabriel Pundrich
Download at https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3496434
"""

import sys
import pandas as pd
import csv
from os import walk

###############################################################################
#CHANGE THIS TO YOUR PATH WHERE THE CODE IS LOCATED
path_env = "/Users/pundrich/Dropbox/gillette-pundrich-grammar/mate/Grammar_distro/"
###############################################################################

path_out=path_code = path_env + "/output/"
path_mda = path_env + "/files_grammar/"

files_to_processed = []
for (dirpath, dirnames, filenames) in walk(path_mda):
    files_to_processed.extend(filenames)
    break



#Exclude Types with high type II error in financial reports
rule_type = ['whitespace',
             'duplication',
             'locale-violation',
             'uncategorized']


#Exclude rules with high type II error in financial reports
rule_subtype = [         
                'A_HUNDREDS',
                'A_INFINITVE',
                'A_LOT_OF_NN',
                'A_MUCH_NN1',
                'A_PLURAL',
                'A_RB_NN',
                'A_UNCOUNTABLE',
                'A_UNCOUNTABLE',
                'ACCEPT_EXCEPT',
                'ACTUAL_EXPERIENCE',
                'ACTUAL_EXPERIENCE',
                'ADDED_BONUS',
                'ADJECTIVE_IN_ATTRIBUTE',
                'ADMIT_ENJOY_VB',
                'ADMIT_ENJOY_VB',
                'ADOPT_TO',
                'ADVANCE_PLANNING',
                'AFFORD_VB',
                'AFFORD_VB',
                'AFFORD_VBG',
                'AGREEMENT_SENT_START',
                'ALL_OF_THE',
                'ALL_OF_THE',
                'ALL_WAYS',
                'ALLOW_TO',
                'ALLOW_TO',
                'ALLY_ALLAY',
                'ALSO_KNOW',
                'ALSO_SENT_END',
                'AM_I',
                'AM_I',
                'AMENABLE_AMENDABLE',
                'AN_ANOTHER',
                'AN_OTHER',
                'ANINFOR_EVERY_DAY',
                'ANY_BODY',
                'ANY_MORE',
                'APART_A_PART',
                'ARCHITECT_VERB',
                'AS_FOLLOW',
                'AS_OPPOSE_TO_AS_OPPOSED_TO',
                'BE_CAUSE',
                'BE_INTEREST_IN',
                'BE_INTEREST_IN',
                'BECAUSE_OF_I',
                'BEEN_PART_AGREEMENT',
                'BEEN_PART_AGREEMENT',
                'BEING_BEGIN',
                'BELIEVE_BELIEF',
                'BELIEVE_BELIEF',
                'BOTH_AS_WELL_AS',
                'BOTH_ENUM',
                'BUILD_OFF_OF',
                'BUY_VBG',
                'BUY_VBG',
                'CAN_BACKUP',
                'CAN_SETUP',
                'CANT',
                'CD_DOZENS_OF',
                'CD_NN',
                'COMMA_MONTH_DATE',
                'COMMA_MONTH_DATE',
                'COMMA_PARENTHESIS_WHITESPACE',
                'COMMA_THAN',
                'COMMON_BOND',
                'COMP_THAN',
                'COMPARISONS_THEN',
                'COMPRISE_OF',
                'COMPRISED_CHIEFLY_OF',
                'COMPRISED_PRINCIPALLY_OF',
                'COMPRISES_OF',
                'COMPRISING_OF',
                'CONFUSION_OF_OUR_OUT',
                'CURRENCY',
                'CURRENCY_SPACE',
                'DID_BASEFORM',
                'DID_PAST',
                'DIE_DICE',
                'DOES_NP_VBZ',
                'DOES_X_HAS',
                'DOUBLE_PUNCTUATION',
                'DOWN_SIDE',
                'DOWNPAYMENT',
                'DT_DT',
                'DT_JJ_NO_NOUN',
                'DT_PRP',
                'DT_RESPONDS',
                'ECONOMIC_ECONOMICAL',
                'ECONOMIC_ECONOMICAL',
                'ECONOMICAL_ECONOMIC',
                'ECONOMICAL_ECONOMIC',
                'EN_A_VS_AN',
                'EN_COMPOUNDS',
                'EN_COMPOUNDS',
                'EN_CONTRACTION_SPELLING',
                'EN_QUOTES',
                'EN_UNPAIRED_BRACKETS',
                'ENGLISH_WORD_REPEAT_BEGINNING_RULE',
                'ENGLISH_WORD_REPEAT_RULE',
                'ENTIRELY_COMPRISED_OF',
                'ET_AL',
                'FEWER_LESS',
                'FEWER_UNCOUNTABLE',
                'FLASHPOINT',
                'FOOT_FEET',
                'FOR_FRO',
                'FORMALLY_KNOWN_AS',
                'FREE_LANCE',
                'FROM_FORM',
                'GAVE_GIVE',
                'GIVE_ADVISE',
                'GOING_TO_VBD',
                'GOT_SHUTDOWN',
                'HAD_VBP',
                'HAD_VBP',
                'HAVE_PART_AGREEMENT',
                'HE_THE',
                'HE_VERB_AGR',
                'HEAD_GEAR',
                'HEAVY_WEIGHT',
                'HELL',
                'HOLLOW_TUBE',
                'HOW_EVER',
                'I_A',
                'I_AM',
                'I_LOWERCASE',
                'I_NEW',
                'IF_IS',
                'IN_A_X_MANNER',
                'IN_A_X_MANNER',
                'IN_JANUARY',
                'IN_PARENTHESIS',
                'IN_PRINCIPAL',
                'IN_TACT',
                'IN_THE_MOMENT',
                'IN_VEIN',
                'INSURE_THAT',
                'IS_COMPRISED_MOSTLY_OF',
                'IS_COMPRISED_OF',
                'IT_IS',
                'IT_IS_JJ_TO_VBG',
                'IT_IS_JJ_TO_VBG',
                'IT_VBZ',
                'KEY_WORDS',
                'KNEW_NEW',
                'LARGE_NUMBER_OF',
                'LARGE_NUMBER_OF',
                'LEAD_ROLL',
                'LEARN_NNNNS_ON_DO',
                'LESS_COMPARATIVE',
                'LESS_DOLLARSMINUTESHOURS',
                'LESS_MORE_THEN',
                'LIFE_TIME',
                'LIGHT_WEIGHT',
                'LING',
                'LOOK_WATCH',
                'LOOSE_LOSE',
                'LOTS_OF_NN',
                'MAKE_SINCE',
                'MAKE_SINCE',
                'MANGER_MANAGER',
                'MANY_FEW_UNCOUNTABLE',
                'MANY_NN',
                'MANY_NN',
                'MANY_NN_U',
                'MASS_AGREEMENT',
                'MAY_BE',
                'META_DATA',
                'MODAL_OF',
                'MORE_A_JJ',
                'MORFOLOGIK_RULE_EN_US',
                'MOST_COMPARATIVE',
                'MUCH_COUNTABLE',
                'MUCH_COUNTABLE',
                'MY_BE',
                'NATION_WIDE',
                'NEAR_BY',
                'NEEDNT_TO_DO_AND_DONT_NEED_DO',
                'NEEDS_FIXED',
                'NEEDS_FIXED',
                'No Error',
                'No MD&A',
                'NODT_DOZEN',
                'NON3PRS_VERB',
                'NON3PRS_VERB',
                'NOT_US1',
                'NOW',
                'NUT_NOT',
                'OF_ANY_OF',
                'OF_ANY_OF',
                'OF_CAUSE',
                'ON_ADDITION',
                'ON_GOING',
                'ONE_OF_THE_ONLY',
                'ONE_ORE',
                'ONE_PLURAL',
                'ONE_PLURAL',
                'ONES',
                'OTHER_THEN',
                'OTHER_WISE_OTHERWISE',
                'OUT_SIDE',
                'OVER_SEAS',
                'PERS_PRONOUN_AGREEMENT_SENT_START',
                'PHRASE_REPETITION',
                'POSSESSIVE_APOSTROPHE',
                'PROGRESSIVE_VERBS',
                'PROGRESSIVE_VERBS',
                'PROVE_PROOF',
                'PRP_MD_CD_IN',
                'PRP_PAST_PART',
                'PRP_RB_NO_VB',
                'RATHER_THEN',
                'SAFE_HAVEN',
                'SAFE_HAVEN',
                'SAFETY_DEPOSIT_BOX',
                'SENTENCE_FRAGMENT',
                'SENTENCE_WHITESPACE',
                'SHORT_CUT',
                'SHOULD_BE_DO',
                'SHOULD_BE_DO',
                'SOME_EXTEND',
                'SOME_NN_VBP',
                'SOME_OF_THE',
                'SOME_OF_THE',
                'SOME_WHAT_JJ',
                'SOME_WHERE',
                'STAND_ALONE',
                'STAND_ALONE_NN',
                'STATUE_OF_LIMITATIONS',
                'SUBSEQUENT_TO',
                'SUBSEQUENT_TO',
                'THE_EXACTLY_THE',
                'THE_NN_AND_THE_NN',
                'THE_NN_AND_THE_NN',
                'THE_PUNCT',
                'THE_PUNCT',
                'THE_SENT_END',
                'THE_SOME_DAY',
                'THE_SUPERLATIVE',
                'THE_SUPERLATIVE',
                'THEIR_IS',
                'THERE_RE_MANY',
                'THERE_RE_MANY',
                'THERE_S_MANY',
                'THIS_NNS',
                'THIS_NNS',
                'THROUGH_OUT',
                'THROUGH_THOROUGH',
                'TO_BATH',
                'TO_NON_BASE',
                'TO_TOO',
                'TOO_TO',
                'UPPERCASE_SENTENCE_START',
                'USE_TO_VERB',
                'USE_TO_VERB',
                'VBZ_VBD',
                'WAS_COMPRISED_OF',
                'WEB_SITE',
                'WED_WE_D',
                'WERE_COMPRISED_OF',
                'WERE_VBB',
                'WHERE_AS',
                'WHICH_COMPRISED_OF',
                'WHITESPACE_RULE',
                'WHO_NOUN',
                'WILL_BE_COMPRISED_OF',
                'WITH_OUT',
                'WITH_THE_EXCEPTION_OF',
                'WITH_THE_EXCEPTION_OF',
                'WOMAN_WOMEN',
                'WORLD_WIDE',
                'YOUR'
                
                ]

import language_check
tool = language_check.LanguageTool('en-US')

filename_output =   "grammar_output"  + ".csv"


num_files_proc = 0
for each_mda in files_to_processed:
    
    
    print("File number: ",num_files_proc)
    #create an empty instance of the dataframe
    dfObj = pd.DataFrame(columns = ['Index'
                                    ,'Offset' 
                                    , 'Length'
                                    ,'Error'
                                    ,'AroundError'
                                    , 'Replacement'                                    
                                    , 'Rule'
                                    , 'Category'
                                    , 'Type'
                                    , 'Message'         
                                    ]) 
    
    print ("\nProcessing File n." + str(each_mda))
    
    try:
        file_mda = open(path_mda+str(each_mda),"r")
        text = file_mda.read()
        size_mda = len(text)
        num_words=0
        
    except:
        print("Problem in reading M&DA")
    
    try:
        if size_mda<200:
            print("MD&A is empty, size is " +  str(len(text)))       
            
            spell_list=[]
            spell_list.append(each_mda) # 2              
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            spell_list.append("No MD&A")
            
            spell_list_final=[]
            spell_list_final.append(spell_list)  
            
        else:
                
            try:
                print("Checking text grammar")
                match = tool.check(text)
            except:
                print("Problem with checking the text")
            

            spell_list_final = []
            
            #list all the errors
            for i in range(0,len(match)):
    
                #get the the wrong word                
                wrong_spelling = text[match[i].offset:match[i].offset+match[i].errorlength]
    
                # ===========================================
                # Rules to avoid false positives 
                # ===========================================
                avoid_rule = True
                for rules_avoidable in rule_type:        
                    if match[i].locqualityissuetype==rules_avoidable:
                        avoid_rule=False
        
                for rule_subtype_avoidable in rule_subtype:
                    if match[i].ruleId==rule_subtype_avoidable:
                        avoid_rule=False
                
                    
                if match[i].ruleId=="MORFOLOGIK_RULE_EN_US" and wrong_spelling=='forma':
                    avoid_rule=False
    
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='assets':
                    avoid_rule=False
        
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='accounts':
                    avoid_rule=False
    
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='earnings':
                    avoid_rule=False
    
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='operations':
                    avoid_rule=False
    
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='receivables':
                    avoid_rule=False
        
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='savings':
                    avoid_rule=False
    
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='securities':
                    avoid_rule=False
    
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='accounting':
                    avoid_rule=False
    
    
                if match[i].ruleId=="EN_A_VS_AN" and ("n/a" in match[i].context):
                    avoid_rule=False
     
                if match[i].ruleId==" " and wrong_spelling==' ':
                    avoid_rule=False
    
                if match[i].ruleId=="POSSESSIVE_APOSTROPHE" and wrong_spelling=='securities':
                    avoid_rule=False
            
                if match[i].category=="Possible Typo":
                    avoid_rule=False
    
    
                # -----------------------------------------------------------------
                # For those without avoidance rule go ahead
                # -----------------------------------------------------------------
                if avoid_rule:
        
                    #print("Select text grammar")
                    spell_list = []
                    
                    #add filename        
                    spell_list.append(each_mda) # 2              
    
                    # get replacement information
                    spell_list.append(match[i].offset) # 2
                
                    spell_list.append(match[i].errorlength) # 4
        
                    spell_list.append(wrong_spelling) # 4
    
                        
                    spell_list.append(match[i].context) # 4
            
                    # get suggested replacements
                    spell_list.append(match[i].replacements) # ["can't", 'cannot']
                                               
                    # get the rules, type and category information of the match
                    spell_list.append(match[i].ruleId) # 'CANT'
                    spell_list.append(match[i].category) # 'TYPOS'
                    spell_list.append(match[i].locqualityissuetype) # 'Other'
                    
                    # getting a friendly message regarding the replacement suggestion
                    spell_list.append(match[i].msg) # 'Did you mean "can\'t" or "cannot"?'
    
    
                    spell_list_final.append(spell_list)  
                    
                    
        print("Saving data for the MD&A")  
            
            
        if len(spell_list_final)==0:
            
            print("No errors found")       
            
            spell_list=[]
            spell_list.append(each_mda) # 2              
            spell_list.append("No Error")
            spell_list.append("No Error")
            spell_list.append("No Error")
            spell_list.append("No Error")
            spell_list.append("No Error")
            spell_list.append("No Error")
            spell_list.append("No Error")
            spell_list.append("No Error")
            spell_list.append("No Error")
            
            spell_list_final=[]
            spell_list_final.append(spell_list)  
            
        dfObj_each = pd.DataFrame(spell_list_final,columns = ['Index'
                                                            ,'Offset' 
                                                            , 'Length'
                                                            ,'Error'
                                                            ,'AroundError'
                                                            , 'Replacement'                                    
                                                            , 'Rule'
                                                            , 'Category'
                                                            , 'Type'
                                                            , 'Message' 
                                                            ]) 
        
        dfObj = dfObj.append(dfObj_each)

        if num_files_proc==0:
            dfObj.to_csv(path_out + filename_output, mode='a',quoting=csv.QUOTE_ALL)
        else:
            dfObj.to_csv(path_out + filename_output, mode='a',header=False,quoting=csv.QUOTE_ALL)
        num_files_proc=num_files_proc+1
    except :
        
        print("Oops!",sys.exc_info(),"occured.")
    
                    
            
            
    
    
        
        
    
    
    
    
    
    
    
