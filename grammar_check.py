#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
From the paper Identifying Financial Reporting Quality from Grammatical Errors in Financial Statements§

@authors: Jacquelyn Gillette and Gabriel Pundrich
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
path_mda = path_env + "/files/"

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
                'ENGLISH_WORD_REPEAT_BEGINNING_RULE',
                'EN_UNPAIRED_BRACKETS',
                'UPPERCASE_SENTENCE_START',
                'CD_NN',
                'DOUBLE_PUNCTUATION',
                'A_INFINITVE',
                'A_PLURAL',
                'A_RB_NN',
                'AFFORD_VBG',
                'AGREEMENT_SENT_START',
                'CD_DOZENS_OF',
                'DT_JJ_NO_NOUN',
                'FEWER_LESS',
                'HAVE_PART_AGREEMENT',
                'HE_VERB_AGR',
                'I_AM',
                'IT_VBZ',
                'LESS_COMPARATIVE',
                'MANY_NN_U',
                'MASS_AGREEMENT',
                'MOST_COMPARATIVE',
                'NODT_DOZEN',
                'PRP_RB_NO_VB',
                'SENTENCE_FRAGMENT',
                'SOME_NN_VBP',
                'THE_SENT_END',
                'TO_NON_BASE',
                'WHO_NOUN',
                'THROUGH_THOROUGH',
                'IN_PRINCIPAL',
                'SUBSEQUENT_TO',
                'MANY_NN',
                'ALL_OF_THE',
                'THE_SUPERLATIVE',
                'LARGE_NUMBER_OF',
                'COMMA_MONTH_DATE',
                'WITH_THE_EXCEPTION_OF',
                'THIS_NNS',
                'EN_COMPOUNDS',
                'SUBSEQUENT_TO',
                'IN_A_X_MANNER',
                'SOME_OF_THE',
                'ACTUAL_EXPERIENCE',
                'ADMIT_ENJOY_VB',
                'OF_ANY_OF',
                'BEEN_PART_AGREEMENT',
                'NEEDS_FIXED',
                'PROGRESSIVE_VERBS',
                'THERE_RE_MANY',
                'ALLOW_TO'
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
                
            
                #To pass the rule "an earnings" suggest wrongly as "a earning"
                if match[i].ruleId=="A_PLURAL" and wrong_spelling=='earnings':
                    avoid_rule=False
    
                if match[i].ruleId=="HAVE_PART_AGREEMENT" and wrong_spelling=='off':
                    avoid_rule=False
        
                if match[i].ruleId=="HE_VERB_AGR" and wrong_spelling=='value':
                    avoid_rule=False
    
                if match[i].ruleId=="LESS_COMPARATIVE" and wrong_spelling=='Less More':
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
    
                if match[i].ruleId=="BEEN_PART_AGREEMENT" and wrong_spelling=='FOB':
                    avoid_rule=False
    
                if match[i].ruleId=="BEEN_PART_AGREEMENT" and wrong_spelling=='interest':
                    avoid_rule=False
    
                if match[i].ruleId=="BEEN_PART_AGREEMENT" and wrong_spelling=='mail':
                    avoid_rule=False
    
                if match[i].ruleId=="BEEN_PART_AGREEMENT" and wrong_spelling=='oil':
                    avoid_rule=False
    
                if match[i].ruleId=="BEEN_PART_AGREEMENT" and wrong_spelling=='Tier':
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
    
                    
            
            
    
    
        
        
    
    
    
    
    
    
    
