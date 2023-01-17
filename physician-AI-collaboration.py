# -*- coding: utf-8 -*-

# script to integrate physician and AI labels
# inputs are : physician_score, AI_score, and weight_i
# outputs are: AI_aided_physician_score, physician_aided_AI_score, 
# average_AI_physician_score, and weighted_average_AI_physician_score.

import numpy as np
import os as os

physician_score = 1 # on a scale of 1 to 8 with 1 being certain it's ARDS 
# negative, and 8 being certainly ARDS positive

AI_score = 0.76 # calibrated AI probabiilty score on a scale of 0-1
AI_score = AI_score * 7 +1 # convert AI score to the score on a scale of 1-8 
# (i.e. physician's rating scale)

weight_i = 0.3 # physician score's weight in the weighted averaging. Valid 
# values are from 0-1.

''' Strategy 1- AI-aided physician: when clinicians are uncertain!'''
if ((physician_score == 4) or (physician_score == 5)):
    AI_aided_physician_score = AI_score
else:
    AI_aided_physician_score = physician_score

''' Strategy 2- physician-aided AI: when machines are uncertain!'''
if ((round(AI_score) == 4) or (round(AI_score) == 5)):
    physician_aided_AI_score = physician_score
else:
    physician_aided_AI_score = AI_score

''' Strategy 3- average of physician and AI'''
average_AI_physician_score = np.mean([physician_score, AI_score])

''' Strategy 4- weighted average of physician and AI'''
weighted_average_AI_physician_score = np.average([physician_score, AI_score], 
                                                 weights = [weight_i, 
                                                            1-weight_i])
