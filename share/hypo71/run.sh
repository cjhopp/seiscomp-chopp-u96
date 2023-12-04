#!/bin/bash

############################################################################
# Copyright (C) 2017 by gempa GmbH                                         #
#                                                                          #
# All Rights Reserved.                                                     #
#                                                                          #
# NOTICE: All information contained herein is, and remains                 #
# the property of gempa GmbH and its suppliers, if any. The intellectual   #
# and technical concepts contained herein are proprietary to gempa GmbH    #
# and its suppliers.                                                       #
# Dissemination of this information or reproduction of this material       #
# is strictly forbidden unless prior written permission is obtained        #
# from gempa GmbH.                                                         #
#                                                                          #
# Author: Dirk Roessler                                                    #
# Email: roessler@gempa.de                                                 #
############################################################################

HYPO71PC_BINARY=Hypo71PC
HYPO71PC_HOME=`dirname $0`

# Jumping into the right directory
cd ${HYPO71PC_HOME}/

## create input file
#echo HYPO71.INP >> input
#echo HYPO71.PRT >> input
#echo HYPO71.OUT >> input
#echo >> input
#echo >> input
#echo >> input
#echo >> input
#echo >> input
#echo >> input
#echo >> input
#echo >> input
#echo >> input
#echo >> input

# Executing binary with input file as argument
${SEISCOMP_ROOT}/bin/$HYPO71PC_BINARY < input

