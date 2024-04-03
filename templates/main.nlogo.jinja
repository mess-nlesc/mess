__includes ["parameters.nls""FieldStorage.nls""ExpansionEvaluation.nls""ExpansionWithinSecondaryCanal.nls""HarvestMemory.nls""AvailableWaterSupply.nls""GateCapacity.nls""FarmersHarvestEvaluation.nls""ExpansionWithin2ndPrimaryCanal.nls"]

to setup
  clear-all
  random-seed 290949
  print (word "current run = " (behaviorspace-run-number))
  show date-and-time                                                                                     ;; shows the current number of the run
  file-open "InitialLayout.txt"                                                                          ;; opens the txt file that contains land type classification and with the start of empty fields
  set InitialLandscape file-read                                                                         ;; sets the land type according to the file
  file-close                                                                                             ;; closes the file, since we are done with

  ( foreach sort patches InitialLandscape                                                                ;; procedure that sorts patches on their land type
    [
      [?1 ?2] -> ask ?1
      [
        set LandType ?2                                                                                  ;; set the land type of this patch to the corresponding land type that is specified in the file
      ]
    ]
  )

  set-default-shape IrrigationVolumes "Irrigation"                                                       ;; represents 1 unit of irrigation volume with a shape of a Irrigation
  set-default-shape RiverVolumes "River"                                                                 ;; represents 1 unit of river water volume with a shape of river
  set-default-shape StorageVolumes "Storage"                                                              ;; represents 1 unit of storage water volume with a shape of a square
  set Q_randomizer 0                                                                                     ;; set the deviation value of Qin_average is 0
  setuppatches                                                                                           ;; define the features of each patch                                                                                              ;; create list to store running output
  reset-ticks                                                                                            ;; resets the time to zero
end

to setuppatches
  ask patches
  [
    if LandType = -3 [set pcolor blue + 2]                  ;; secondary canal
    if LandType = -2 [set pcolor blue ]                     ;; primary canal
    if LandType = -1
    [
      set pcolor red
      if pycor > 14
      [
        set ReadyforGCDecision_PrimaryCanal false                             ;; ready for GC change (boolean)
      ]
    ]                       ;; gate
    if LandType = 0  [set pcolor blue - 1]                  ;; river
    if LandType = 1                                         ;; fellow fields
    [
      set pcolor brown
      set IrrigationDemand 0
    ]
    if LandType = 2                                         ;; barley fields
    [
      set pcolor green
      set IrrigationDemand BarleyIrrigationDemand           ;; set irrigation demand to barley irrigation demand
      set BarleyQuality 4                                   ;; set quality of barley to 3, since it starts healty
      set HarvestCycle BarleyHarvestCycle                   ;; set the harvest cycle to barley
    ]
    if LandType = 3                                         ;; water storage
    [
      set pcolor grey
      set CompareOnceAYear true                                ;; the procedure of comparing the harvest every year
      set CompareEveryTwoYearsPrimary false                    ;; the procedure of comparing the harvest every two years along the primary canal
      set CompareEveryTwoYearsSecondary false                  ;; the procedure of comparing the harvest every two years along the secondary canal
      set ComparisonCountDownPrimary ComparisonTime
      set ComparisonCountDownSecondary ComparisonTime
;;;;;;these for meet good harvest first
     set ContinuouslySameHarvestYearProcedure_1year_1st? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_1year_2nd? False          ;; use to record the continuously same good harvest year with 1 year, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_1year_3rd? False          ;; use to record the continuously same good harvest year with 1 year, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_1year_4th? False          ;; use to record the continuously same good harvest year with 1 year, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_1year_5th? False          ;; use to record the continuously same good harvest year with 1 year, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_1year_6th? False          ;; use to record the continuously same good harvest year with 1 year, appear at the 6th time
     set ContinuouslySameHarvestYearProcedure_1year_7th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 7th time
     set ContinuouslySameHarvestYearProcedure_1year_8th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 8th time
     set ContinuouslySameHarvestYearProcedure_1year_9th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 9th time
     set ContinuouslySameHarvestYearProcedure_1year_10th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 10th time
     set ContinuouslySameHarvestYearProcedure_1year_11th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 11th time
     set ContinuouslySameHarvestYearProcedure_1year_12th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 12th time
     set ContinuouslySameHarvestYearProcedure_1year_13th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 13th time
     set ContinuouslySameHarvestYearProcedure_1year_14th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 14th time
     set ContinuouslySameHarvestYearProcedure_1year_15th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 15th time
     set ContinuouslySameHarvestYearProcedure_1year_16th? False           ;; use to record the continuously same good harvest year with 1 year, appear at the 16th time

     set ContinuouslySameHarvestYearProcedure_2years_1st? False         ;; use to record the continuously same good harvest year with 2 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_2years_2nd? False         ;; use to record the continuously same good harvest year with 2 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_2years_3rd? False         ;; use to record the continuously same good harvest year with 2 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_2years_4th? False         ;; use to record the continuously same good harvest year with 2 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_2years_5th? False         ;; use to record the continuously same good harvest year with 2 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_2years_6th? False         ;; use to record the continuously same good harvest year with 2 years, appear at the 6th time
     set ContinuouslySameHarvestYearProcedure_2years_7th? False          ;; use to record the continuously same good harvest year with 2 years, appear at the 7th time
     set ContinuouslySameHarvestYearProcedure_2years_8th? False          ;; use to record the continuously same good harvest year with 2 years, appear at the 8th time

     set ContinuouslySameHarvestYearProcedure_3years_1st? False         ;; use to record the continuously same good harvest year with 3 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_3years_2nd? False         ;; use to record the continuously same good harvest year with 3 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_3years_3rd? False         ;; use to record the continuously same good harvest year with 3 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_3years_4th? False         ;; use to record the continuously same good harvest year with 3 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_3years_5th? False         ;; use to record the continuously same good harvest year with 3 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_3years_6th? False         ;; use to record the continuously same good harvest year with 3 years, appear at the 6th time

     set ContinuouslySameHarvestYearProcedure_4years_1st? False         ;; use to record the continuously same good harvest year with 4 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_4years_2nd? False         ;; use to record the continuously same good harvest year with 4 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_4years_3rd? False         ;; use to record the continuously same good harvest year with 4 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_4years_4th? False         ;; use to record the continuously same good harvest year with 4 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_4years_5th? False         ;; use to record the continuously same good harvest year with 4 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_4years_6th? False         ;; use to record the continuously same good harvest year with 4 years, appear at the 6th time

     set ContinuouslySameHarvestYearProcedure_5years_1st? False          ;; use to record the continuously same good harvest year with 5 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_5years_2nd? False         ;; use to record the continuously same good harvest year with 5 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_5years_3rd? False         ;; use to record the continuously same good harvest year with 5 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_5years_4th? False         ;; use to record the continuously same good harvest year with 5 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_5years_5th? False         ;; use to record the continuously same good harvest year with 5 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_5years_6th? False         ;; use to record the continuously same good harvest year with 5 years, appear at the 6th time

     set ContinuouslySameHarvestYearProcedure_6years_1st? False         ;; use to record the continuously same good harvest year with 6 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_6years_2nd? False         ;; use to record the continuously same good harvest year with 6 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_6years_3rd? False         ;; use to record the continuously same good harvest year with 6 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_6years_4th? False         ;; use to record the continuously same good harvest year with 6 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_6years_5th? False         ;; use to record the continuously same good harvest year with 6 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_6years_6th? False         ;; use to record the continuously same good harvest year with 6 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_1year_1st? False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_1year_2nd? False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_1year_3rd? False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_1year_4th? False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_1year_5th? False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_1year_6th? False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 6th time
     set ContinuouslyPoorHarvestYearProcedure_1year_7th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 7th time
     set ContinuouslyPoorHarvestYearProcedure_1year_8th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 8th time
     set ContinuouslyPoorHarvestYearProcedure_1year_9th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 9th time
     set ContinuouslyPoorHarvestYearProcedure_1year_10th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 10th time
     set ContinuouslyPoorHarvestYearProcedure_1year_11th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 11th time
     set ContinuouslyPoorHarvestYearProcedure_1year_12th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 12th time
     set ContinuouslyPoorHarvestYearProcedure_1year_13th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 13th time
     set ContinuouslyPoorHarvestYearProcedure_1year_14th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 14th time
     set ContinuouslyPoorHarvestYearProcedure_1year_15th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 15th time
     set ContinuouslyPoorHarvestYearProcedure_1year_16th? False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 16th time

     set ContinuouslyPoorHarvestYearProcedure_2years_1st? False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_2years_2nd? False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_2years_3rd? False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_2years_4th? False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_2years_5th? False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_2years_6th? False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 6th time
     set ContinuouslyPoorHarvestYearProcedure_2years_7th? False          ;; use to record the continuously Poor harvest year with 2 years, appear at the 7th time
     set ContinuouslyPoorHarvestYearProcedure_2years_8th? False          ;; use to record the continuously Poor harvest year with 2 years, appear at the 8th time

     set ContinuouslyPoorHarvestYearProcedure_3years_1st? False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_3years_2nd? False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_3years_3rd? False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_3years_4th? False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_3years_5th? False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_3years_6th? False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_4years_1st? False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_4years_2nd? False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_4years_3rd? False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_4years_4th? False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_4years_5th? False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_4years_6th? False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_5years_1st? False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_5years_2nd? False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_5years_3rd? False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_5years_4th? False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_5years_5th? False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_5years_6th? False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_6years_1st? False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_6years_2nd? False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_6years_3rd? False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_6years_4th? False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_6years_5th? False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_6years_6th? False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 6th time

       set CountDownExpansion1_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 1st time
       set CountDownExpansion1_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 2nd time
       set CountDownExpansion1_3 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 3rd time
       set CountDownExpansion1_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 4th time
       set CountDownExpansion1_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 5th time
       set CountDownExpansion1_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 6th time
       set CountDownExpansion1_7 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 7th time
       set CountDownExpansion1_8 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 8th time
       set CountDownExpansion1_9 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 9th time
       set CountDownExpansion1_10 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 10th time
       set CountDownExpansion1_11 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 11th time
       set CountDownExpansion1_12 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 12th time
       set CountDownExpansion1_13 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 13th time
       set CountDownExpansion1_14 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 14th time
       set CountDownExpansion1_15 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 15th time
       set CountDownExpansion1_16 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 16th time

       set CountDownExpansion2_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 1st time
       set CountDownExpansion2_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 2nd time
       set CountDownExpansion2_3 (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously same good harvest year with 2 year, appear at the 3rd time
       set CountDownExpansion2_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 4th time
       set CountDownExpansion2_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 5th time
       set CountDownExpansion2_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 6th time
       set CountDownExpansion2_7 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 7th time
       set CountDownExpansion2_8 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 8th time

       set CountDownExpansion3_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 1st time
       set CountDownExpansion3_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 2nd time
       set CountDownExpansion3_3 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 3rd time
       set CountDownExpansion3_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 4th time
       set CountDownExpansion3_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 5th time
       set CountDownExpansion3_6 (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously same good harvest year with 3 year, appear at the 6th time

       set CountDownExpansion4_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 1st time
       set CountDownExpansion4_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 2nd time
       set CountDownExpansion4_3 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 3rd time
       set CountDownExpansion4_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 4th time
       set CountDownExpansion4_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 5th time
       set CountDownExpansion4_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 6th time

       set CountDownExpansion5_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 1st time
       set CountDownExpansion5_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 2nd time
       set CountDownExpansion5_3 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 3rd time
       set CountDownExpansion5_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 4th time
       set CountDownExpansion5_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 5th time
       set CountDownExpansion5_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 6th time

       set CountDownExpansion6_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 1st time
       set CountDownExpansion6_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 2nd time
       set CountDownExpansion6_3 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 3rd time
       set CountDownExpansion6_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 4th time
       set CountDownExpansion6_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 5th time
       set CountDownExpansion6_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 6th time

       set CountDownMovement1_1 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 1st time
       set CountDownMovement1_2 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 2nd time
       set CountDownMovement1_3 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 3rd time
       set CountDownMovement1_4 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 4th time
       set CountDownMovement1_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 5th time
       set CountDownMovement1_6 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 6th time
       set CountDownMovement1_7 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 7th time
       set CountDownMovement1_8 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 8th time
       set CountDownMovement1_9 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 9th time
       set CountDownMovement1_10 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 10th time
       set CountDownMovement1_11 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 11th time
       set CountDownMovement1_12 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 12th time
       set CountDownMovement1_13 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 13th time
       set CountDownMovement1_14 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 14th time
       set CountDownMovement1_15 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 15th time
       set CountDownMovement1_16 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 16th time

       set CountDownMovement2_1 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 1st time
       set CountDownMovement2_2 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 2nd time
       set CountDownMovement2_3 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 3rd time
       set CountDownMovement2_4 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 4th time
       set CountDownMovement2_5 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 5th time
       set CountDownMovement2_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 2 year, appear at the 6th time
       set CountDownMovement2_7 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 7th time
       set CountDownMovement2_8 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 8th time

       set CountDownMovement3_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 1st time
       set CountDownMovement3_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 2nd time
       set CountDownMovement3_3 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 3rd time
       set CountDownMovement3_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 4th time
       set CountDownMovement3_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 5th time
       set CountDownMovement3_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 6th time

       set CountDownMovement4_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 4 year, appear at the 1st time
       set CountDownMovement4_2 (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously Poor harvest year with 4 year, appear at the 2nd time
       set CountDownMovement4_3 (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously Poor harvest year with 4 year, appear at the 3rd time
       set CountDownMovement4_4 (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 4 year, appear at the 4th time
       set CountDownMovement4_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 4 year, appear at the 5th time
       set CountDownMovement4_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 4 year, appear at the 6th time

       set CountDownMovement5_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 1st time
       set CountDownMovement5_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 2nd time
       set CountDownMovement5_3 (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously Poor harvest year with 5 year, appear at the 3rd time
       set CountDownMovement5_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 4th time
       set CountDownMovement5_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 5th time
       set CountDownMovement5_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 6th time

       set CountDownMovement6_1 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 1st time
       set CountDownMovement6_2 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 2nd time
       set CountDownMovement6_3 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 3rd time
       set CountDownMovement6_4 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 4th time
       set CountDownMovement6_5 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 5th time
       set CountDownMovement6_6 (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 6th time

;;;;;;these for meet poor harvest first
     set ContinuouslySameHarvestYearProcedure_1year_1st?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_1year_2nd?p False          ;; use to record the continuously same good harvest year with 1 year, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_1year_3rd?p False          ;; use to record the continuously same good harvest year with 1 year, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_1year_4th?p False          ;; use to record the continuously same good harvest year with 1 year, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_1year_5th?p False          ;; use to record the continuously same good harvest year with 1 year, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_1year_6th?p False          ;; use to record the continuously same good harvest year with 1 year, appear at the 6th time
     set ContinuouslySameHarvestYearProcedure_1year_7th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 7th time
     set ContinuouslySameHarvestYearProcedure_1year_8th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 8th time
     set ContinuouslySameHarvestYearProcedure_1year_9th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 9th time
     set ContinuouslySameHarvestYearProcedure_1year_10th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 10th time
     set ContinuouslySameHarvestYearProcedure_1year_11th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 11th time
     set ContinuouslySameHarvestYearProcedure_1year_12th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 12th time
     set ContinuouslySameHarvestYearProcedure_1year_13th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 13th time
     set ContinuouslySameHarvestYearProcedure_1year_14th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 14th time
     set ContinuouslySameHarvestYearProcedure_1year_15th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 15th time
     set ContinuouslySameHarvestYearProcedure_1year_16th?p False           ;; use to record the continuously same good harvest year with 1 year, appear at the 16th time

     set ContinuouslySameHarvestYearProcedure_2years_1st?p False         ;; use to record the continuously same good harvest year with 2 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_2years_2nd?p False         ;; use to record the continuously same good harvest year with 2 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_2years_3rd?p False         ;; use to record the continuously same good harvest year with 2 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_2years_4th?p False         ;; use to record the continuously same good harvest year with 2 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_2years_5th?p False         ;; use to record the continuously same good harvest year with 2 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_2years_6th?p False         ;; use to record the continuously same good harvest year with 2 years, appear at the 6th time
     set ContinuouslySameHarvestYearProcedure_2years_7th?p False          ;; use to record the continuously same good harvest year with 2 years, appear at the 7th time
     set ContinuouslySameHarvestYearProcedure_2years_8th?p False          ;; use to record the continuously same good harvest year with 2 years, appear at the 8th time

     set ContinuouslySameHarvestYearProcedure_3years_1st?p False         ;; use to record the continuously same good harvest year with 3 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_3years_2nd?p False         ;; use to record the continuously same good harvest year with 3 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_3years_3rd?p False         ;; use to record the continuously same good harvest year with 3 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_3years_4th?p False         ;; use to record the continuously same good harvest year with 3 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_3years_5th?p False         ;; use to record the continuously same good harvest year with 3 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_3years_6th?p False         ;; use to record the continuously same good harvest year with 3 years, appear at the 6th time

     set ContinuouslySameHarvestYearProcedure_4years_1st?p False         ;; use to record the continuously same good harvest year with 4 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_4years_2nd?p False         ;; use to record the continuously same good harvest year with 4 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_4years_3rd?p False         ;; use to record the continuously same good harvest year with 4 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_4years_4th?p False         ;; use to record the continuously same good harvest year with 4 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_4years_5th?p False         ;; use to record the continuously same good harvest year with 4 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_4years_6th?p False         ;; use to record the continuously same good harvest year with 4 years, appear at the 6th time

     set ContinuouslySameHarvestYearProcedure_5years_1st?p False          ;; use to record the continuously same good harvest year with 5 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_5years_2nd?p False         ;; use to record the continuously same good harvest year with 5 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_5years_3rd?p False         ;; use to record the continuously same good harvest year with 5 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_5years_4th?p False         ;; use to record the continuously same good harvest year with 5 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_5years_5th?p False         ;; use to record the continuously same good harvest year with 5 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_5years_6th?p False         ;; use to record the continuously same good harvest year with 5 years, appear at the 6th time

     set ContinuouslySameHarvestYearProcedure_6years_1st?p False         ;; use to record the continuously same good harvest year with 6 years, appear at the 1st time
     set ContinuouslySameHarvestYearProcedure_6years_2nd?p False         ;; use to record the continuously same good harvest year with 6 years, appear at the 2nd time
     set ContinuouslySameHarvestYearProcedure_6years_3rd?p False         ;; use to record the continuously same good harvest year with 6 years, appear at the 3rd time
     set ContinuouslySameHarvestYearProcedure_6years_4th?p False         ;; use to record the continuously same good harvest year with 6 years, appear at the 4th time
     set ContinuouslySameHarvestYearProcedure_6years_5th?p False         ;; use to record the continuously same good harvest year with 6 years, appear at the 5th time
     set ContinuouslySameHarvestYearProcedure_6years_6th?p False         ;; use to record the continuously same good harvest year with 6 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_1year_1st?p False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_1year_2nd?p False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_1year_3rd?p False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_1year_4th?p False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_1year_5th?p False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_1year_6th?p False          ;; use to record the continuously Poor harvest year with 1 year, appear at the 6th time
     set ContinuouslyPoorHarvestYearProcedure_1year_7th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 7th time
     set ContinuouslyPoorHarvestYearProcedure_1year_8th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 8th time
     set ContinuouslyPoorHarvestYearProcedure_1year_9th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 9th time
     set ContinuouslyPoorHarvestYearProcedure_1year_10th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 10th time
     set ContinuouslyPoorHarvestYearProcedure_1year_11th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 11th time
     set ContinuouslyPoorHarvestYearProcedure_1year_12th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 12th time
     set ContinuouslyPoorHarvestYearProcedure_1year_13th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 13th time
     set ContinuouslyPoorHarvestYearProcedure_1year_14th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 14th time
     set ContinuouslyPoorHarvestYearProcedure_1year_15th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 15th time
     set ContinuouslyPoorHarvestYearProcedure_1year_16th?p False           ;; use to record the continuously Poor harvest year with 1 year, appear at the 16th time

     set ContinuouslyPoorHarvestYearProcedure_2years_1st?p False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_2years_2nd?p False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_2years_3rd?p False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_2years_4th?p False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_2years_5th?p False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_2years_6th?p False         ;; use to record the continuously Poor harvest year with 2 years, appear at the 6th time
     set ContinuouslyPoorHarvestYearProcedure_2years_7th?p False          ;; use to record the continuously Poor harvest year with 2 years, appear at the 7th time
     set ContinuouslyPoorHarvestYearProcedure_2years_8th?p False          ;; use to record the continuously Poor harvest year with 2 years, appear at the 8th time

     set ContinuouslyPoorHarvestYearProcedure_3years_1st?p False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_3years_2nd?p False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_3years_3rd?p False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_3years_4th?p False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_3years_5th?p False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_3years_6th?p False         ;; use to record the continuously Poor harvest year with 3 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_4years_1st?p False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_4years_2nd?p False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_4years_3rd?p False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_4years_4th?p False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_4years_5th?p False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_4years_6th?p False         ;; use to record the continuously Poor harvest year with 4 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_5years_1st?p False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_5years_2nd?p False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_5years_3rd?p False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_5years_4th?p False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_5years_5th?p False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_5years_6th?p False         ;; use to record the continuously Poor harvest year with 5 years, appear at the 6th time

     set ContinuouslyPoorHarvestYearProcedure_6years_1st?p False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 1st time
     set ContinuouslyPoorHarvestYearProcedure_6years_2nd?p False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 2nd time
     set ContinuouslyPoorHarvestYearProcedure_6years_3rd?p False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 3rd time
     set ContinuouslyPoorHarvestYearProcedure_6years_4th?p False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 4th time
     set ContinuouslyPoorHarvestYearProcedure_6years_5th?p False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 5th time
     set ContinuouslyPoorHarvestYearProcedure_6years_6th?p False         ;; use to record the continuously Poor harvest year with 6 years, appear at the 6th time

       set CountDownExpansion1_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 1st time
       set CountDownExpansion1_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 2nd time
       set CountDownExpansion1_3p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 3rd time
       set CountDownExpansion1_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 4th time
       set CountDownExpansion1_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 5th time
       set CountDownExpansion1_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 6th time
       set CountDownExpansion1_7p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 7th time
       set CountDownExpansion1_8p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 8th time
       set CountDownExpansion1_9p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 9th time
       set CountDownExpansion1_10p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 10th time
       set CountDownExpansion1_11p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 11th time
       set CountDownExpansion1_12p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 12th time
       set CountDownExpansion1_13p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 13th time
       set CountDownExpansion1_14p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 14th time
       set CountDownExpansion1_15p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 15th time
       set CountDownExpansion1_16p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 1 year, appear at the 16th time

       set CountDownExpansion2_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 1st time
       set CountDownExpansion2_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 2nd time
       set CountDownExpansion2_3p (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously same good harvest year with 2 year, appear at the 3rd time
       set CountDownExpansion2_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 4th time
       set CountDownExpansion2_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 5th time
       set CountDownExpansion2_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 6th time
       set CountDownExpansion2_7p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 7th time
       set CountDownExpansion2_8p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 2 year, appear at the 8th time

       set CountDownExpansion3_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 1st time
       set CountDownExpansion3_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 2nd time
       set CountDownExpansion3_3p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 3rd time
       set CountDownExpansion3_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 4th time
       set CountDownExpansion3_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 3 year, appear at the 5th time
       set CountDownExpansion3_6p (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously same good harvest year with 3 year, appear at the 6th time

       set CountDownExpansion4_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 1st time
       set CountDownExpansion4_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 2nd time
       set CountDownExpansion4_3p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 3rd time
       set CountDownExpansion4_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 4th time
       set CountDownExpansion4_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 5th time
       set CountDownExpansion4_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 4 year, appear at the 6th time

       set CountDownExpansion5_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 1st time
       set CountDownExpansion5_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 2nd time
       set CountDownExpansion5_3p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 3rd time
       set CountDownExpansion5_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 4th time
       set CountDownExpansion5_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 5th time
       set CountDownExpansion5_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 5 year, appear at the 6th time

       set CountDownExpansion6_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 1st time
       set CountDownExpansion6_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 2nd time
       set CountDownExpansion6_3p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 3rd time
       set CountDownExpansion6_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 4th time
       set CountDownExpansion6_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 5th time
       set CountDownExpansion6_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously same good harvest year with 6 year, appear at the 6th time

       set CountDownMovement1_1p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 1st time
       set CountDownMovement1_2p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 2nd time
       set CountDownMovement1_3p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 3rd time
       set CountDownMovement1_4p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 4th time
       set CountDownMovement1_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 5th time
       set CountDownMovement1_6p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 1 year, appear at the 6th time
       set CountDownMovement1_7p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 7th time
       set CountDownMovement1_8p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 8th time
       set CountDownMovement1_9p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 9th time
       set CountDownMovement1_10p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 10th time
       set CountDownMovement1_11p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 11th time
       set CountDownMovement1_12p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 12th time
       set CountDownMovement1_13p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 13th time
       set CountDownMovement1_14p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 14th time
       set CountDownMovement1_15p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 15th time
       set CountDownMovement1_16p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 1 year, appear at the 16th time

       set CountDownMovement2_1p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 1st time
       set CountDownMovement2_2p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 2nd time
       set CountDownMovement2_3p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 3rd time
       set CountDownMovement2_4p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 4th time
       set CountDownMovement2_5p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 5th time
       set CountDownMovement2_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 2 year, appear at the 6th time
       set CountDownMovement2_7p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 7th time
       set CountDownMovement2_8p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 2 year, appear at the 8th time

       set CountDownMovement3_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 1st time
       set CountDownMovement3_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 2nd time
       set CountDownMovement3_3p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 3rd time
       set CountDownMovement3_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 4th time
       set CountDownMovement3_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 5th time
       set CountDownMovement3_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 3 year, appear at the 6th time

       set CountDownMovement4_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 4 year, appear at the 1st time
       set CountDownMovement4_2p (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously Poor harvest year with 4 year, appear at the 2nd time
       set CountDownMovement4_3p (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously Poor harvest year with 4 year, appear at the 3rd time
       set CountDownMovement4_4p (ComparisonCountDownForCanalExpansion + 1)                                      ;; use to record the continuously Poor harvest year with 4 year, appear at the 4th time
       set CountDownMovement4_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 4 year, appear at the 5th time
       set CountDownMovement4_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 4 year, appear at the 6th time

       set CountDownMovement5_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 1st time
       set CountDownMovement5_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 2nd time
       set CountDownMovement5_3p (ComparisonCountDownForCanalExpansion + 1)                                    ;; use to record the continuously Poor harvest year with 5 year, appear at the 3rd time
       set CountDownMovement5_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 4th time
       set CountDownMovement5_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 5th time
       set CountDownMovement5_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 5 year, appear at the 6th time

       set CountDownMovement6_1p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 1st time
       set CountDownMovement6_2p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 2nd time
       set CountDownMovement6_3p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 3rd time
       set CountDownMovement6_4p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 4th time
       set CountDownMovement6_5p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 5th time
       set CountDownMovement6_6p (ComparisonCountDownForCanalExpansion + 1)                                     ;; use to record the continuously Poor harvest year with 6 year, appear at the 6th time
    ]
    if LandType = 4  [set pcolor green + 2]                  ;; none watercourse or fields
    if LandType = 5  [set pcolor black]                      ;; edge of the world, without function
    if LandType = 6                                         ;; fields when at preirrigation stagee
    [
      set pcolor sky
      ;set IrrigationDemand Pre-IrrigationDemand
    ]
    set ReadyForBarley false                                 ;; fields can not be cultivated straight away from the start
    set AlreadyWithBarley false                              ;; all fields without barley in he begainning

    set F11NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF11 CountDownForHarvestMemory
    set F11NeverWithLand? True
    set CountDownLandF11 CountDownForWaterAvailability

    set F14NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF14 CountDownForHarvestMemory
    set F14NeverWithLand? True
    set CountDownLandF14 CountDownForWaterAvailability

    set F15NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF15 CountDownForHarvestMemory
    set F15NeverWithLand? True
    set CountDownLandF15 CountDownForWaterAvailability

    set F16NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF16 CountDownForHarvestMemory
    set F16NeverWithLand? True
    set CountDownLandF16 CountDownForWaterAvailability

    set F17NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF17 CountDownForHarvestMemory
    set F17NeverWithLand? True
    set CountDownLandF17 CountDownForWaterAvailability

    set F20NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF20 CountDownForHarvestMemory
    set F20NeverWithLand? True
    set CountDownLandF20 CountDownForWaterAvailability

    set F21NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF21 CountDownForHarvestMemory
    set F21NeverWithLand? True
    set CountDownLandF21 CountDownForWaterAvailability

    set F22NeverWithBarley? true                                           ;; use to record the farmer has the first harvest or not
    set CountDownBarleyF22 CountDownForHarvestMemory
    set F22NeverWithLand? True
    set CountDownLandF22 CountDownForWaterAvailability
  ]
end

to go
  set Year floor (ticks / 365) + 1
  set day ticks                                                              ;; time scale: daily
  RiverInflow                                                                   ;; runs the procedure of RiverFlow

  if ticks >= 3 and ticks <= 36500;21900;18250;10950;7300;3650                                                   ;; the first sowing year
  [
    with-local-randomness
    [
      Flow-to-Primary-canal                                                       ;; initial setting includes one canal, let river volume moves to the primary canal first
      Flow-to-Secondary-canal                                                     ;; dig a secondary canal
      GateCapacity                                                                ;; set the capacity of head gate and farmer's gate
      GateCapacity_F1-10                                                          ;; set the capacity of head gate and farmer's gate along the primary canal F1-10
      GateCapacity_F11-13                                                         ;; set the capacity of farmer's gate along the secondary canal F11-13
      GateCapacity_F11-14                                                         ;; set the capacity of farmer's gate along the secondary canal F11-14
      GateCapacity_F11-15                                                         ;; set the capacity of farmer's gate along the secondary canal F11-15
      GateCapacity_F11-16                                                         ;; set the capacity of farmer's gate along the secondary canal F11-16
      GateCapacity_F17-19                                                         ;; set the capacity of farmer's gate along the 2nd primary canal F17-19
      GateCapacity_F17-20                                                         ;; set the capacity of farmer's gate along the 2nd primary canal F17-20
      GateCapacity_F17-21                                                         ;; set the capacity of farmer's gate along the 2nd primary canal F17-21
      GateCapacity_F17-22                                                         ;; set the capacity of farmer's gate along the 2nd primary canal F17-22
      GateFlow                                                                    ;; water volume turns head at the gate and set the volume
      FieldStorage                                                                ;; set the current storage of the storage patches
      FieldStorageOverFlow                                                        ;; set the capacity of the storage patches
      FirstSowChoice
      FieldPreparation1
      InitialSow                                                                  ;; create the situation in the first year
      Irrigation                                                                  ;; set irrigation actions
      TrackFieldsReceivedWater                                                    ;; record the amount of received water of each field
      WaterStress                                                                 ;; set different levels of water stress to barley
      Harvest                                                                     ;; set the harvest actions
      FarmersToTalBarley                                                          ;; caculate the total barley of each farmer
      FarmersHarvestSituationPerYear                                              ;; record the number of harvest fields and barley yields of each farmer in each year
      FallowFields                                                                ;; set the fields after harvest
      FarmersHarvestEvaluation                                                    ;; for GC variation, farmers evaluation for expanding canal from the 1st primary canal to the 1st secondary canal
      HarvestMemory                                                               ;; set the barley harvest to each farmer (set as a seperate file)
      AvailableWaterSupply                                                        ;; set the available suppy water to each farmer (set as a seperate file)
      BarleySowSelection                                                          ;; set the barley sowing selection actions, farmers need to make decision based on the harvest and available water
      FieldPreparation2
      FieldPreparation2-sub
      FieldPreparation3
      FieldPreparation4
      FieldPreparation5
      ExpansionEvaluation                                                         ;; at the end of 20th year, evaluate farmers' harvest and to decide to expand or movement
      FarmersHarvestEvaluation_SecondayCanal                                      ;; for GC variation, farmers evaluation for expanding farmers along the secondary canal
      FarmersExpansionEvaluation_SecondayCanal                                    ;; evaluate farmers' harvest situation and then decide to expand more farmers along the secondary canal or not
      FarmersExpansionEvaluation_2ndPrimaryCanalF17-19                            ;; the procedure shows the expansion from the secondary canal to the 2nd primary canal
      FarmersExpansionEvaluation_2ndPrimaryCanal                                  ;; the procedure shows the expansion within the 2nd primary canal from F17-19 to F20,, 21, 22.
      FarmersHarvestEvaluationF17-22                                              ;; the procedure used to evaluate GC variation for F17-22
      Outflow                                                                     ;; set the outflow of the river and canals
      set-label                                                                   ;; runs the procedure set-label
    ]
  ]

  if ticks = 36500                                                               ;; run the model with 10;20;30;50 years
  [
    print (word "This Run (" (behaviorspace-run-number) ") is done!")                  ;; displays that the run is done
    stop
  ]

  tick
end

to RiverInflow
  ask RiverVolumes [fd 1]

  let rand random 3                                                                     ;; local variable to randomize the inflow, 3 possibilities: average, lower than average, higher than average

  if rand = 0
  [                                                                         ;; inflow lower than average
    ifelse Qin_randomizer > 0
    [
      set Q_randomizer ( (random Qin_randomizer ) + 1 )                             ;; local variable that determines the downwards deviation from the average
    ]
    [
      set Q_randomizer 0                                                             ;; ifelse the randomizer should be 0
    ]

    let number-of-RiverVolumes (Qin_average - Q_randomizer)                           ;; generate inflow of sum (average - randomizer)

     create-RiverVolumes number-of-RiverVolumes
     [
       setxy 25 19
       set color blue + 2                                                              ;; set color of turtle to dark blue
       set size 0.5                                                                    ;; set size of turtle to 0.5
       set heading 180
    ]
  ]

  if rand = 1
  [                                                                 ;; inflow is average
    let number-of-RiverVolumes  Qin_average
    create-RiverVolumes number-of-RiverVolumes                                  ;; generate inflow of Qin_average
    [
      setxy 25 19
      set color blue + 2                                             ;; set color of turtle to dark blue
      set size 0.5                                                   ;; set size of turtle to 0.5
      set heading 180
    ]
  ]

  if rand = 2
  [                                                     ;; inflow is higher than average
    ifelse Qin_randomizer > 0
    [
      set Q_randomizer ( ( random Qin_randomizer ) + 1 )        ;; local variable that determines the downwards deviation from the average
    ]
    [
      set Q_randomizer 0                                        ;; ifelse the randomizer should be 0
    ]

    let number-of-RiverVolumes ( Qin_average + Q_randomizer )

     create-RiverVolumes number-of-RiverVolumes                    ;; generate inflow of sum (average + randomizer)
     [
       setxy 25 19
       set color blue + 2                                          ;; set color of turtle to dark blue
       set size 0.5                                                ;; set size of turtle to 0.5
       set heading 180
    ]
  ]
end

to Flow-to-Primary-canal
  ask patches with [pcolor = blue - 1]
  [
    if pxcor = 25 and pycor = 17
    [
      ifelse [pcolor] of patch (pxcor - 1) pycor != blue
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here
        [
          lt 90
          fd 1
        ]
      ]
      [
        ifelse [LandType] of patch 44 18 != 4
        [
          ;; F17-19
          ifelse [pcolor] of patch (pxcor - 9) pycor != red
          [
            ask n-of (round ((count RiverVolumes-here) * (16 / 19))) RiverVolumes-here
            [
              lt 90
              fd 1
            ]
            ;;the rest moves to the 2nd primary canal
            ask n-of (count RiverVolumes-here) RiverVolumes-here                                               ;; flow to the secondary canal
            [
              rt 90
              fd 1
            ]
          ]
          [
            ;; F17-20
            ifelse [pcolor] of patch (pxcor - 11) pycor != red
            [
              ask n-of (round ((count RiverVolumes-here) * (16 / 20))) RiverVolumes-here
              [
                lt 90
                fd 1
              ]
              ;;the rest moves to the 2nd primary canal
              ask n-of (count RiverVolumes-here) RiverVolumes-here                                               ;; flow to the secondary canal
              [
                rt 90
                fd 1
              ]
            ]
            [
              ;; F17-21
              ifelse [pcolor] of patch (pxcor - 13) pycor != red
              [
                ask n-of (round ((count RiverVolumes-here) * (16 / 21))) RiverVolumes-here
                [
                  lt 90
                  fd 1
                ]
                ;;the rest moves to the 2nd primary canal
                ask n-of (count RiverVolumes-here) RiverVolumes-here                                               ;; flow to the secondary canal
                [
                  rt 90
                  fd 1
                ]
              ]
              [
                ;; F17-22
                ask n-of (round ((count RiverVolumes-here) * (16 / 22))) RiverVolumes-here
                [
                  lt 90
                  fd 1
                ]
                ;;the rest moves to the 2nd primary canal
                ask n-of (count RiverVolumes-here) RiverVolumes-here                                               ;; flow to the secondary canal
                [
                  rt 90
                  fd 1
                ]
              ]
            ]
          ]
        ]
        [
          ;;poor harvest and expanded
          ;; F17-19
          if [pcolor] of patch (pxcor - 9) pycor != red
          [
            ask n-of (round ((count RiverVolumes-here) * (7 / 10))) RiverVolumes-here
            [
              lt 90
              fd 1
            ]
            ;;the rest moves to the 2nd primary canal
            ask n-of (count RiverVolumes-here) RiverVolumes-here                                               ;; flow to the secondary canal
            [
              rt 90
              fd 1
            ]
          ]
        ]
      ]
    ]
  ]
end

to Flow-to-Secondary-canal
  ask patches with [pcolor = blue]
  [
    if pxcor = 38 and pycor = 17
    [
      if [pcolor] of patch pxcor (pycor - 1) = blue + 2
      [
        ;;canal expansion because of good harvest
        if [pcolor] of patch (pxcor + 7) (pycor + 2) != green + 2                                          ;; expansion
        [
          ;; F11-13
          ifelse [pcolor] of patch pxcor (pycor - 10) != red + 2
          [
            ask n-of (round ((count RiverVolumes-here) * (6 / 8))) RiverVolumes-here                          ;; stay in the primary canal
            [
              fd 1
            ]
          ]
          [
            ;; F11-14
            ifelse [pcolor] of patch pxcor (pycor - 12) != red + 2
            [
              ask n-of (round ((count RiverVolumes-here) * (5 / 9))) RiverVolumes-here                          ;; stay in the primary canal
              [
                fd 1
              ]
            ]
            [
              ;;F11-15
              ifelse [pcolor] of patch pxcor (pycor - 14) != red + 2
              [
                ask n-of (round ((count RiverVolumes-here) * (1 / 2))) RiverVolumes-here                          ;; stay in the primary canal
                [
                  fd 1
                ]
              ]
              [
                ;; F11-16
                ask n-of (round ((count RiverVolumes-here) * (5 / 11))) RiverVolumes-here                          ;; stay in the primary canal
                [
                  fd 1
                ]
              ]
            ]
          ]
        ]

        ;;canal expansion because of poor harvest
        if [pcolor] of patch (pxcor + 7) (pycor + 2) = green + 2                                            ;; movement
        [
          ;; F11-13
          ifelse [pcolor] of patch pxcor (pycor - 10) != red + 2
          [
            ask n-of (round ((count RiverVolumes-here) * (2 / 5))) RiverVolumes-here                          ;; stay in the primary canal
            [
              fd 1
            ]
          ]
          [
            ;; F11-14
            ifelse [pcolor] of patch pxcor (pycor - 12) != red + 2
            [
              ask n-of (round ((count RiverVolumes-here) * (2 / 6))) RiverVolumes-here                          ;; stay in the primary canal
              [
                fd 1
              ]
            ]
            [
              ;;F11-15
              ifelse [pcolor] of patch pxcor (pycor - 14) != red + 2
              [
                ask n-of (round ((count RiverVolumes-here) * (2 / 7))) RiverVolumes-here                          ;; stay in the primary canal
                [
                  fd 1
                ]
              ]
              [
                ;; F11-16
                ask n-of (round ((count RiverVolumes-here) * (2 / 8))) RiverVolumes-here                          ;; stay in the primary canal
                [
                  fd 1
                ]
              ]
            ]
          ]
        ]

        ;;the rest moves to the secondary canal
        ask n-of (count RiverVolumes-here) RiverVolumes-here                                               ;; flow to the secondary canal
        [
          rt 90
          fd 1
        ]
      ]
    ]
  ]
end

to GateFlow
  ;;for gates along the primary canal
  ask patches with [pcolor = red and pycor = 17]                                                                                                         ;; ask gates at the right side of the river
  [
  ;; for F1-10
  if pxcor = 28
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 32
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 36
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 41
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 45 and [pcolor] of patch pxcor (pycor + 1) = grey
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 49 and [pcolor] of patch pxcor (pycor + 1) = grey
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 30
  [
    ifelse [CurrentStorage] of patch pxcor (pycor - 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [rt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 34
  [
    ifelse [CurrentStorage] of patch pxcor (pycor - 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [rt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 43
  [
    ifelse [CurrentStorage] of patch pxcor (pycor - 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [rt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 47 and [pcolor] of patch pxcor (pycor - 1) = grey
  [
    ifelse [CurrentStorage] of patch pxcor (pycor - 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [rt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
      ]
    ]
    [
    ]
  ]
  ;; for F17-22
  if pxcor = 22
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [rt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 20
  [
    ifelse [CurrentStorage] of patch pxcor (pycor - 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 18
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [rt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 16
  [
    ifelse [CurrentStorage] of patch pxcor (pycor - 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 14
  [
    ifelse [CurrentStorage] of patch pxcor (pycor + 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [rt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
      ]
    ]
    [
    ]
  ]
  if pxcor = 12
  [
    ifelse [CurrentStorage] of patch pxcor (pycor - 1) < MaximunStorageOfStoragePatch
    [
      ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
      [
        ask n-of QGateMax RiverVolumes-here [lt 90]
      ]
      [
        ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
      ]
    ]
    [
    ]
  ]
]
  ;;for gates along the secondary canal, F11-16
  ask patches with [pcolor = red + 2 and pxcor = 38]                                                                                                         ;; ask gates at the right side of the river
  [
    ;F11
    if pycor = 13
    [
      ifelse [CurrentStorage] of patch (pxcor - 1) pycor < MaximunStorageOfStoragePatch
      [
        ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
        [
          ask n-of QGateMax RiverVolumes-here [rt 90]
        ]
        [
          ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
        ]
      ]
      [
      ]
    ]
    ;F12
    if pycor = 11
    [
      ifelse [CurrentStorage] of patch (pxcor + 1) pycor < MaximunStorageOfStoragePatch
      [
        ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
        [
          ask n-of QGateMax RiverVolumes-here [lt 90]
        ]
        [
          ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
        ]
      ]
      [
      ]
    ]
    ;F13
    if pycor = 9
    [
      ifelse [CurrentStorage] of patch (pxcor - 1) pycor < MaximunStorageOfStoragePatch
      [
        ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
        [
          ask n-of QGateMax RiverVolumes-here [rt 90]
        ]
        [
          ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
        ]
      ]
      [
      ]
    ]
    ;F14
    if pycor = 7
    [
      ifelse [CurrentStorage] of patch (pxcor + 1) pycor < MaximunStorageOfStoragePatch
      [
        ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
        [
          ask n-of QGateMax RiverVolumes-here [lt 90]
        ]
        [
          ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
        ]
      ]
      [
      ]
    ]
    ;F15
    if pycor = 5
    [
      ifelse [CurrentStorage] of patch (pxcor - 1) pycor < MaximunStorageOfStoragePatch
      [
        ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
        [
          ask n-of QGateMax RiverVolumes-here [rt 90]
        ]
        [
          ask n-of (count RiverVolumes-here) RiverVolumes-here [rt 90]
        ]
      ]
      [
      ]
    ]
    ;F16
    if pycor = 3
    [
      ifelse [CurrentStorage] of patch (pxcor + 1) pycor < MaximunStorageOfStoragePatch
      [
        ifelse (count RiverVolumes-here - QGateMax) > 0                                                                                                  ;; if the river volumes here more than te gate capacity
        [
          ask n-of QGateMax RiverVolumes-here [lt 90]
        ]
        [
          ask n-of (count RiverVolumes-here) RiverVolumes-here [lt 90]
        ]
      ]
      [
      ]
    ]
  ]
end


to FieldStorageOverFlow
  ask patches with [pcolor = grey]                                                                       ;; ask the fields which used to store the irrigation water
  [
    if CurrentStorage > MaximunStorageOfStoragePatch                                                     ;; if the current storage exceeds the maximum storage
    [
      ask n-of (CurrentStorage - MaximunStorageOfStoragePatch) StorageVolumes-here [die]                 ;; ask the extra storage volumes to die (so they go out the system)
      set CurrentStorage MaximunStorageOfStoragePatch                                                    ;; set current storage to the FirsIrrigationDemand
    ]
  ]
end

to FirstSowChoice
  ask patches with [LandType = 1]                                                                                                   ;; ask fallow fields
  [
    if ReadyForBarley = true
    [
      if pxcor > 25
      [
        ;;for gates along the 1st primary canal
        if pycor > 14
        [
          if ([CurrentStorage] of patch (pxcor + 1) pycor) > 0      ;;field1
          [
            if count HarvestBarleyRecords-here = 0
            [
              set LandType 6
              set pcolor sky
            ]
          ]
        ]
        ;;for gates along the secondary canal
        if  pycor < 15
        [
          ifelse pxcor > 35 and pxcor < 41 and pycor > 8 and pycor < 16
          [
            if ([CurrentStorage] of patch pxcor (pycor - 1)) > 0      ;;field1
            [
              if count HarvestBarleyRecords-here = 0
              [
                set LandType 6
                set pcolor sky
              ]
            ]
          ]
          [
            if ([CurrentStorage] of patch pxcor (pycor - 1)) > 0      ;;field1
            [
              if count HarvestBarleyRecords-here = 0
              [
                set LandType 6
                set pcolor sky
              ]
            ]
          ]
        ]
      ]
      if pxcor < 25
      [
        if ([CurrentStorage] of patch (pxcor + 1) pycor) > 0      ;;field1
        [
          if count HarvestBarleyRecords-here = 0
          [
            set LandType 6
            set pcolor sky
          ]
        ]
      ]
    ]
  ]
end

to FieldPreparation1
  ask patches with [LandType = 6]                                                                        ;; ask fields that need pre irrigation, always means field1 in the first sowing year
  [
    set IrrigationDemand Pre-IrrigationDemand
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;for gates along the primary canal;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    if pycor > 14
    [
      if ([LandType] of patch (pxcor + 1) pycor) = 3                                                       ;; storage patch
      [
        set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                   ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                      ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                        ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
        ]

        let Use-Field-IrrigationVolumes1 Field-IrrigationVolume1                                             ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor + 1) pycor) = 3
        [
          ask patch (pxcor + 1) pycor
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes1)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of Use-Field-IrrigationVolumes1 StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]
        sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
        if count IrrigationVolumes-here >= IrrigationDemand
        [
           set IrrigationStatus "Irrigated"
        ]
      ]
    ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;for gates along the secondary canal;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    if pycor < 15
    [
      if ([LandType] of patch pxcor (pycor - 1)) = 3                                                       ;; storage patch
      [
        set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                   ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                      ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                        ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
        ]

        let Use-Field-IrrigationVolumes1 Field-IrrigationVolume1                                             ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch pxcor (pycor - 1)) = 3
        [
          ask patch pxcor (pycor - 1)
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes1)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of Use-Field-IrrigationVolumes1 StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]
        sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
        if count IrrigationVolumes-here >= IrrigationDemand
        [
           set IrrigationStatus "Irrigated"
        ]
      ]
    ]
    if count IrrigationVolumes-here > 0
    [
      set Counter (count IrrigationVolumes-here)
      ifelse Counter >= IrrigationDemand                                                    ;; if the current storage exceeds the maximum storage
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]                ;; ask the extra storage volumes to die (so they go out the system)
        set ReceivedWater1 IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater1 Counter
        set plabel Counter
      ]
      show word "ReceivedWater1:" ReceivedWater1
    ]

    if ReceivedWater1 >= 82                                                             ;; if farmers start barley > 0 and there is storage volume in the storage patch
    [
      set LandType 2                                                                                            ;; sowing barley
      set pcolor green
      set HarvestCycle (BarleyHarvestCycle + 1)                                                                 ;; set the harvest cycle, add one because at the end of this procedure, 1 day will already be substracted even when reset
      set IrrigationMemory (BarleyIrrigationMemory + 1)
      if pycor > 14
      [
        ask HarvestBarleyRecords [die]
      ]
      if pycor < 15
      [
        ask HarvestBarleyRecords-here [die]
      ]
    ]
  ]
end

to InitialSow
  ask patches with [LandType = 2]                                                                              ;; barley field
  [
    set BarleyQuality 4
    set IrrigationDemand BarleyIrrigationDemand
    BarleyGrowth
  ]
end

to BarleyGrowth                                                                                           ;; create barley
  if (count BarleyPlants-here) < 1
  [
    sprout-BarleyPlants 1
    [
      set shape "plant"
      set size 0.1
      set color black
    ]
  ]
end

to Irrigation
  ask patches with [LandType = 2]                                                                         ;; ask fields with barley
  [
    set IrrigationMemory (IrrigationMemory - 1)                                                           ;; for each tick the irrigation memory is reduced by 1, means minus one day

    if IrrigationMemory < 1                                                                               ;; fields need to be irrigated
    [
      IrrigationBehaviour1                                                                                 ;; run irrigation action
      if Field-IrrigationVolume1 > 0                                                                       ;; if there is a irrigation volume in the barley field1
      [
        set IrrigationMemory (IrrigationMemory + BarleyIrrigationMemory)                                  ;; reset the irrigation memory of barley
      ]
    ]
    if IrrigationMemory < 1                                                                               ;; fields need to be irrigated
    [                                                                                 ;; run irrigation action
      IrrigationBehaviour2
      if Field-IrrigationVolume2 > 0                                                                       ;; if there is a irrigation volume in the barley field2
      [
        set IrrigationMemory (IrrigationMemory + BarleyIrrigationMemory)                                  ;; reset the irrigation memory of barley
      ]
    ]
    if IrrigationMemory < 1                                                                               ;; fields need to be irrigated
    [
      IrrigationBehaviour3
      if Field-IrrigationVolume3 > 0                                                                       ;; if there is a irrigation volume in the barley field2
      [
        set IrrigationMemory (IrrigationMemory + BarleyIrrigationMemory)                                  ;; reset the irrigation memory of barley
      ]
    ]
    if IrrigationMemory < 1                                                                               ;; fields need to be irrigated
    [
      IrrigationBehaviour4
      if Field-IrrigationVolume4 > 0                                                                       ;; if there is a irrigation volume in the barley field2
      [
        set IrrigationMemory (IrrigationMemory + BarleyIrrigationMemory)                                  ;; reset the irrigation memory of barley
      ]
    ]
    if IrrigationMemory < 1                                                                               ;; fields need to be irrigated
    [
      IrrigationBehaviour5
       if Field-IrrigationVolume5 > 0                                                                       ;; if there is a irrigation volume in the barley field2
      [
        set IrrigationMemory (IrrigationMemory + BarleyIrrigationMemory)                                  ;; reset the irrigation memory of barley
      ]
    ]
  ]
end
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;if expand a new field, the irrigation priority is satisfy the previous field when received water is lower than the irrigation demand;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;here, head gate capacity, storage capacity and river inflow, downstream farmers' welling should be considered;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
to IrrigationBehaviour1
  if pycor > 17
  [
    ;;if field1 needs irrigation
    if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
    [
      set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
      [
        set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
      ]
      [
        set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
      ]

      let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
      [
        ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
        [
          set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
          ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
  ]

  if pycor < 17                                                                                              ;; irrigation of the primary canal and the secondary canal should be separately
  [
    ;;if field1 needs irrigation
    ;;the primary canal
    if pycor > 14
    [
      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
      [
        set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
        ]

        let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

        if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
        [
          ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
            ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
    ]
    ;;the second canal
    if pycor < 15
    [
      if pxcor < 38                                                                                              ;; left side of the secondary canal
      [
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
      if pxcor > 38                                                                                              ;; right side of the secondary canal
      [
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
    ]
  ]

  if count IrrigationVolumes-here > 0
  [
    set Counter (count IrrigationVolumes-here)
    ifelse any? BarleyPlants-here
    [
      ifelse Counter >= IrrigationDemand
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]
        set ReceivedWater IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater Counter
        set plabel Counter
      ]
    ]
    [
      set ReceivedWater 0
      set plabel 0
    ]
    show word "ReceivedWater:" ReceivedWater
  ]
end

to IrrigationBehaviour2
  if pycor > 17
  [
    ;;if field1 needs irrigation
    if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
    [
      set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch
      ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
      [
        set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
      ]
      [
        set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
      ]
      let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
      [
        ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
        [
          set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
          ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
        ]
      ]
      sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 and field2 need irrigation
    if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [                                                                                                          ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume2 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume2 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
      [
        ask patch (pxcor + 1) (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
  ]

  if pycor < 17
  [
    ;;the primary canal
    if pycor > 14
    [
      ;;if field1 needs irrigation
      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
      [
        set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
        ]

        let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

        if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
        [
          ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
            ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 and field2 need irrigation
      if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [                                                               ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor + 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume2 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume2 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
        [
          ask patch (pxcor + 1) (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
    ]
    ;;the secondary canal
    if pycor < 15
    [
      if pxcor < 38                                                                                              ;; left side of the secondary canal
      [
        ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
          [
            ask patch (pxcor + 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
      if pxcor > 38                                                                                              ;; right side of the secondary canal
      [
        ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
          [
            ask patch (pxcor - 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
    ]
  ]

  if count IrrigationVolumes-here > 0
  [
    set Counter (count IrrigationVolumes-here)
    ifelse any? BarleyPlants-here
    [
      ifelse Counter >= IrrigationDemand
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]
        set ReceivedWater IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater Counter
        set plabel Counter
      ]
    ]
    [
      set ReceivedWater 0
      set plabel 0
    ]
    show word "ReceivedWater:" ReceivedWater
  ]
end

to IrrigationBehaviour3
  if pycor > 17
  [
    ;;if field1 needs irrigation
    if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
    [
      set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
      [
        set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
      ]
      [
        set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
      ]

      let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
      [
        ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
        [
          set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
          ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 and field2 need irrigation
    if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [                                                               ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume2 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume2 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
      [
        ask patch (pxcor + 1) (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 field2, and field3 need irrigation
    if ([LandType] of patch pxcor (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [
      set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch pxcor (pycor - 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume3 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume3 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch pxcor (pycor - 1)) = 3
      [
        ask patch pxcor (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
  ]

  if pycor < 17
  [
    ;;the primary canal
    if pycor > 14
    [
      ;;if field1 needs irrigation
      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
      [
        set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
        ]

        let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

        if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
        [
          ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
            ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 and field2 need irrigation
      if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [                                                               ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor + 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume2 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume2 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
        [
          ask patch (pxcor + 1) (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 field2, and field3 need irrigation
      if ([LandType] of patch pxcor (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [
        set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch pxcor (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume3 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume3 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch pxcor (pycor + 1)) = 3
        [
          ask patch pxcor (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
    ]
    ;;the secondary canal
    if pycor < 15
    [
      if pxcor < 38                                                                                            ;; left side of the secondary canal
      [
        ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
          [
            ask patch (pxcor + 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, and field3 need irrigation
        if ([LandType] of patch (pxcor + 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume3 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume3 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) pycor) = 3
          [
            ask patch (pxcor + 1) pycor
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
      if pxcor > 38                                                                                            ;; right side of the secondary canal
      [
        ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
          [
            ask patch (pxcor - 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, and field3 need irrigation
        if ([LandType] of patch (pxcor - 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume3 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume3 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) pycor) = 3
          [
            ask patch (pxcor - 1) pycor
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
    ]
  ]

  if count IrrigationVolumes-here > 0
  [
    set Counter (count IrrigationVolumes-here)
    ifelse any? BarleyPlants-here
    [
      ifelse Counter >= IrrigationDemand
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]
        set ReceivedWater IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater Counter
        set plabel Counter
      ]
    ]
    [
      set ReceivedWater 0
      set plabel 0
    ]
    show word "ReceivedWater:" ReceivedWater
  ]
end

to IrrigationBehaviour4
  if pycor > 17
  [
    ;;if field1 needs irrigation
    if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
    [
      set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
      [
        set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
      ]
      [
        set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
      ]

      let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
      [
        ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
        [
          set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
          ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 and field2 need irrigation
    if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [                                                               ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume2 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume2 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
      [
        ask patch (pxcor + 1) (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 field2, and field3 need irrigation
    if ([LandType] of patch pxcor (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [
      set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch pxcor (pycor - 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume3 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume3 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch pxcor (pycor - 1)) = 3
      [
        ask patch pxcor (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 field2, field3, and field4 need irrigation
    if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [
      set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor - 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume4 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume4 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
      [
        ask patch (pxcor - 1) (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
  ]

  if pycor < 17
  [
    ;;the primary canal
    if pycor > 14
    [
      ;;if field1 needs irrigation
      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
      [
        set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
        ]

        let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

        if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
        [
          ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
            ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 and field2 need irrigation
      if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [                                                               ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor + 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume2 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume2 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
        [
          ask patch (pxcor + 1) (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 field2, and field3 need irrigation
      if ([LandType] of patch pxcor (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [
        set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch pxcor (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume3 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume3 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch pxcor (pycor + 1)) = 3
        [
          ask patch pxcor (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 field2, field3, and field4 need irrigation
      if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [
        set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume4 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume4 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
        [
          ask patch (pxcor - 1) (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
    ]
    ;;the secondary canal
    if pycor < 15
    [
      if pxcor < 38                                                                                            ;; left side of the secondary canal
      [
        ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
          [
            ask patch (pxcor + 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, and field3 need irrigation
        if ([LandType] of patch (pxcor + 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume3 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume3 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) pycor) = 3
          [
            ask patch (pxcor + 1) pycor
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, field3, and field4 need irrigation
        if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume4 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume4 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
          [
            ask patch (pxcor + 1) (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
      if pxcor > 38                                                                                              ;; right side of the secondary canal
      [
        ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
          [
            ask patch (pxcor - 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, and field3 need irrigation
        if ([LandType] of patch (pxcor - 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume3 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume3 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) pycor) = 3
          [
            ask patch (pxcor - 1) pycor
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, field3, and field4 need irrigation
        if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume4 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume4 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
          [
            ask patch (pxcor - 1) (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
    ]
  ]

  if count IrrigationVolumes-here > 0
  [
    set Counter (count IrrigationVolumes-here)
    ifelse any? BarleyPlants-here
    [
      ifelse Counter >= IrrigationDemand
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]
        set ReceivedWater IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater Counter
        set plabel Counter
      ]
    ]
    [
      set ReceivedWater 0
      set plabel 0
    ]
    show word "ReceivedWater:" ReceivedWater
  ]
end

to IrrigationBehaviour5
  if pycor > 17
  [
    ;;if field1 needs irrigation
    if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
    [
      set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
      [
        set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
      ]
      [
        set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
      ]

      let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
      [
        ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
        [
          set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
          ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [die]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 and field2 need irrigation
    if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [                                                               ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume2 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume2 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
      [
        ask patch (pxcor + 1) (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 field2, and field3 need irrigation
    if ([LandType] of patch pxcor (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [
      set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch pxcor (pycor - 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume3 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume3 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch pxcor (pycor - 1)) = 3
      [
        ask patch pxcor (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 field2, field3, and field4 need irrigation
    if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
    [
      set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor - 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume4 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume4 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
      [
        ask patch (pxcor - 1) (pycor - 1)
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
    ;;if field1 field2, field3, field4, and field5 need irrigation
    if ([LandType] of patch (pxcor - 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
    [
      set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
      set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

      ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
      [
        set Field-IrrigationVolume5 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
      ]
      [
        if CurrentStorage <= 0
        [
          set Field-IrrigationVolume5 0
        ]
        if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
        [
          set Field-IrrigationVolume5 CurrentStorage
        ]
      ]

      let Use-Field-IrrigationVolumes5 Field-IrrigationVolume5                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

      if ([LandType] of patch (pxcor - 1) pycor) = 3
      [
        ask patch (pxcor - 1) pycor
        [
          set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4 - Use-Field-IrrigationVolumes5)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Field-IrrigationVolume4 + Use-Field-IrrigationVolumes5) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
      ]

      sprout-IrrigationVolumes Field-IrrigationVolume5                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
      [
        set color turquoise
        set size 0.5
        set heading 0
      ]
    ]
  ]

  if pycor < 17
  [
    ;;the primary canal
    if pycor > 14
    [
      ;;if field1 needs irrigation
      if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
      [
        set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                       ;; set the current storage of the field to the current storage in the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
        ]

        let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

        if ([pcolor] of patch (pxcor + 1) pycor) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
        [
          ask  patch (pxcor + 1) pycor                                                                         ;; ask the storage patch
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
            ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 and field2 need irrigation
      if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [                                                               ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor + 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume2 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume2 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
        [
          ask patch (pxcor + 1) (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 field2, and field3 need irrigation
      if ([LandType] of patch pxcor (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [
        set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch pxcor (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume3 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume3 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch pxcor (pycor + 1)) = 3
        [
          ask patch pxcor (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 field2, field3, and field4 need irrigation
      if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
      [
        set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume4 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume4 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
        [
          ask patch (pxcor - 1) (pycor + 1)
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
      ;;if field1 field2, field3, field4, and field5 need irrigation
      if ([LandType] of patch (pxcor - 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
      [
        set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
        set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

        ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume5 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          if CurrentStorage <= 0
          [
            set Field-IrrigationVolume5 0
          ]
          if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
          [
            set Field-IrrigationVolume5 CurrentStorage
          ]
        ]

        let Use-Field-IrrigationVolumes5 Field-IrrigationVolume5                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

        if ([LandType] of patch (pxcor - 1) pycor) = 3
        [
          ask patch (pxcor - 1) pycor
          [
            set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4 - Use-Field-IrrigationVolumes5)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Field-IrrigationVolume4 + Use-Field-IrrigationVolumes5) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
        ]

        sprout-IrrigationVolumes Field-IrrigationVolume5                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
      ]
    ]
    if pycor < 15
    [
      if pxcor < 38                                                                                              ;; left side of the secondary canal
      [
      ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
          [
            ask patch (pxcor + 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, and field3 need irrigation
        if ([LandType] of patch (pxcor + 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume3 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume3 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) pycor) = 3
          [
            ask patch (pxcor + 1) pycor
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, field3, and field4 need irrigation
        if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor + 1) (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume4 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume4 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
          [
            ask patch (pxcor + 1) (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, field3, field4, and field5 need irrigation
        if ([LandType] of patch pxcor (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch pxcor (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume5 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume5 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume5 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes5 Field-IrrigationVolume5                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch pxcor (pycor + 1)) = 3
          [
            ask patch pxcor (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4 - Use-Field-IrrigationVolumes5)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Field-IrrigationVolume4 + Use-Field-IrrigationVolumes5) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume5                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
      if pxcor > 38                                                                                              ;; right side of the secondary canal
      [
        ;;if field1 needs irrigation
        if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                          ;; searches for the storage patch and if it is the storage patch, set the current storage, field1
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                       ;; set the current storage of the field to the current storage in the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                              ;; if there is more or equal storage than the water demand of the barley
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                          ;; set irrigation volume to the irrigation demand
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                            ;; if there is not sufficient storage to provide the irrigation demand, set the irrigation volume to the maximum amount, which is the currently available volume in the storage patch
          ]

          let Use-Field-IrrigationVolume1 Field-IrrigationVolume1                                                  ;; local variable that  allows the storage in the storage patch to be reduced according to the amount of water used for irrigation of barley on a field patch

          if ([pcolor] of patch pxcor (pycor - 1)) = grey                                                        ;; searches for the storage patch and if it is the storage patch, set the current storage
          [
            ask  patch pxcor (pycor - 1)                                                                         ;; ask the storage patch
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolume1)                                   ;; update the current storage to a lower amount because water was used for irrigation
              ask n-of Use-Field-IrrigationVolume1 StorageVolumes-here [ die ]                                    ;; ask storage volumes on the reservoir to die, the amount is equal to the amount of supplied irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume1                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 and field2 need irrigation
        if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [                                                               ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor - 1)) - Field-IrrigationVolume1)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume2 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume2 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume2 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
          [
            ask patch (pxcor - 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Use-Field-IrrigationVolumes2)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Use-Field-IrrigationVolumes2) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume2                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, and field3 need irrigation
        if ([LandType] of patch (pxcor - 1) pycor) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) pycor) - Field-IrrigationVolume1 - Field-IrrigationVolume2)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume3 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume3 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) pycor) = 3
          [
            ask patch (pxcor - 1) pycor
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Use-Field-IrrigationVolumes3)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Use-Field-IrrigationVolumes3) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume3                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, field3, and field4 need irrigation
        if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch (pxcor - 1) (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume4 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume4 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume4 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes4 Field-IrrigationVolume4                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
          [
            ask patch (pxcor - 1) (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Use-Field-IrrigationVolumes4)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Use-Field-IrrigationVolumes4) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume4                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        ;;if field1 field2, field3, field4, and field5 need irrigation
        if ([LandType] of patch pxcor (pycor + 1)) = 3                                                       ;; storage patch, if field1 need preirrigation
        [
          set IrrigationDemand Pre-IrrigationDemand                                                          ;; fellow field has no irrigation demand
          set CurrentStorage (([CurrentStorage] of patch pxcor (pycor + 1)) - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4)        ;; set currentstorage of the barley field to the currentstorage of the storage patch

          ifelse CurrentStorage >= IrrigationDemand                                                                ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume5 IrrigationDemand                                                           ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            if CurrentStorage <= 0
            [
              set Field-IrrigationVolume5 0
            ]
            if CurrentStorage > 0 and  CurrentStorage < IrrigationDemand
            [
              set Field-IrrigationVolume5 CurrentStorage
            ]
          ]

          let Use-Field-IrrigationVolumes5 Field-IrrigationVolume5                                                   ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field

          if ([LandType] of patch pxcor (pycor + 1)) = 3
          [
            ask patch pxcor (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Field-IrrigationVolume1 - Field-IrrigationVolume2 - Field-IrrigationVolume3 - Field-IrrigationVolume4 - Use-Field-IrrigationVolumes5)                               ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of (Field-IrrigationVolume1 + Field-IrrigationVolume2 + Field-IrrigationVolume3 + Field-IrrigationVolume4 + Use-Field-IrrigationVolumes5) StorageVolumes-here [die]                                  ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
          ]

          sprout-IrrigationVolumes Field-IrrigationVolume5                                                       ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
      ]
    ]
  ]
  if count IrrigationVolumes-here > 0
  [
    set Counter (count IrrigationVolumes-here)
    ifelse Counter >= IrrigationDemand                                                                   ;; if the current storage exceeds the maximum storage
    [
      ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]                                 ;; ask the extra storage volumes to die (so they go out the system)
      set ReceivedWater IrrigationDemand
      set plabel IrrigationDemand
    ]
    [
      set ReceivedWater Counter
      set plabel Counter
    ]
    show word "ReceivedWater:" ReceivedWater
  ]
end

to TrackFieldsReceivedWater;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;improvement needed;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patches with [LandType = 2]
  [
    if Harvestcycle = 145
    [
      ask IrrigationVolumes-here [die]
      set plabel 0
    ]
    if HarvestCycle = 109
    [
      set ReceivedWater2 ReceivedWater
      ask IrrigationVolumes-here [die]
      set plabel 0
    ]
    if HarvestCycle = 73
    [
      set ReceivedWater3 ReceivedWater
      ask IrrigationVolumes-here [die]
      set plabel 0
    ]
    if HarvestCycle = 37
    [
      set ReceivedWater4 ReceivedWater
      ask IrrigationVolumes-here [die]
      set plabel 0
    ]
    if HarvestCycle = 1
    [
      set ReceivedWater5 ReceivedWater
      ask IrrigationVolumes-here [die]
      set plabel 0
    ]
  ]
end

to WaterStress
  ask patches with [LandType = 2]                                                                          ;; ask patches with barley
  [
    if IrrigationMemory <= -24
    [
      ask BarleyPlants-here [die]
      set LandType 1                                                                          ;; after harvest, the field becomes fellow again
      set pcolor brown                                                                        ;; set color to brown
      set IrrigationDemand 0                                                                  ;; set irrigation demand to 0 since fellow fields don't need water
      set BarleyQuality 0                                                                     ;; set quality of barley to 0 since fellow fields don't have barley
      set FallowCountDown (Year * 365 - Day)                                                  ;; set the FallowCountDown to 2 so that after this time step fallowCountDown is 1, because after this procedure the procedure fallowfields substracts 1 of the value, and then would result into the possiblity to regrow straight away
      set ReadyForBarley false                                                                ;; set readyForCrops to false since it is not straight away ready for new crops
      set ReceivedWater1 0
      set ReceivedWater2 0
      set ReceivedWater3 0
      set ReceivedWater4 0
      set ReceivedWater5 0
    ]

    set FieldReceivedWater-Stage1 (ReceivedWater1 + ReceivedWater2)                                      ;; local variables to record the fields received water at each calculation stage
    if FieldReceivedWater-Stage1 = 164
    [
      set BarleyQuality1 4
    ]
    if FieldReceivedWater-Stage1 >= 82 and FieldReceivedWater-Stage1 < 164
     [
      set BarleyQuality1 3
    ]
    if FieldReceivedWater-Stage1 > 0 and FieldReceivedWater-Stage1 < 82
    [
      set BarleyQuality1 1
    ]
    if FieldReceivedWater-Stage1 = 0 or ReceivedWater1 = 0 or ReceivedWater2 = 0
    [
      set BarleyQuality1 0
    ]

    set FieldReceivedWater-Stage2 (ReceivedWater3 + ReceivedWater4)
    if FieldReceivedWater-Stage2 = 164
    [
      set BarleyQuality2 4
    ]
    if FieldReceivedWater-Stage2 >= 82 and FieldReceivedWater-Stage2 < 164
    [
      set BarleyQuality2 3
    ]
    if FieldReceivedWater-Stage2 >= 41 and FieldReceivedWater-Stage2 < 82
    [
      set BarleyQuality2 2
    ]
    if FieldReceivedWater-Stage2 > 0 and FieldReceivedWater-Stage2 < 41
    [
      set BarleyQuality2 1
    ]
    if FieldReceivedWater-Stage2 = 0 or ReceivedWater3 = 0 or ReceivedWater4 = 0
    [
      set BarleyQuality2 0
    ]

    set FieldReceivedWater-Stage3 ReceivedWater5
    if FieldReceivedWater-Stage3 = 82
    [
      set BarleyQuality3 4
    ]
    if FieldReceivedWater-Stage3 >= 41 and FieldReceivedWater-Stage3 < 82
    [
      set BarleyQuality3 3
    ]
    if FieldReceivedWater-Stage3 > 0 and FieldReceivedWater-Stage3 < 42
    [
      set BarleyQuality3 1
    ]
    if FieldReceivedWater-Stage3 = 0
    [
      set BarleyQuality3 0
    ]
  ]
end

to Harvest
  ask patches with [LandType = 2]                                                            ;; ask fields with barley
  [
    if HarvestCycle = 0                                                                      ;; if barley is ready to be harvested
    [
      set HarvestCycle (BarleyHarvestCycle + 1)                                              ;; reset the harvest cycle, add one because at the end of this procedure, 1 day will already be substracted even when reset

      if BarleyQuality1 = 4 and BarleyQuality2 = 4 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY6]
      if BarleyQuality1 = 4 and BarleyQuality2 = 4 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY5]
      if BarleyQuality1 = 4 and BarleyQuality2 = 4 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 4 and BarleyQuality2 = 4 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 4 and BarleyQuality2 = 3 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY5]
      if BarleyQuality1 = 4 and BarleyQuality2 = 3 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY4]
      if BarleyQuality1 = 4 and BarleyQuality2 = 3 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 4 and BarleyQuality2 = 3 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 4 and BarleyQuality2 = 2 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY4]
      if BarleyQuality1 = 4 and BarleyQuality2 = 2 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY3]
      if BarleyQuality1 = 4 and BarleyQuality2 = 2 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 4 and BarleyQuality2 = 2 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 4 and BarleyQuality2 = 1 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 4 and BarleyQuality2 = 1 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 4 and BarleyQuality2 = 1 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 4 and BarleyQuality2 = 1 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 4 and BarleyQuality2 = 0 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 4 and BarleyQuality2 = 0 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 4 and BarleyQuality2 = 0 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 4 and BarleyQuality2 = 0 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 4 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY5]
      if BarleyQuality1 = 3 and BarleyQuality2 = 4 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY4]
      if BarleyQuality1 = 3 and BarleyQuality2 = 4 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 3 and BarleyQuality2 = 4 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 3 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY4]
      if BarleyQuality1 = 3 and BarleyQuality2 = 3 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY3]
      if BarleyQuality1 = 3 and BarleyQuality2 = 3 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 3 and BarleyQuality2 = 3 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 2 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY3]
      if BarleyQuality1 = 3 and BarleyQuality2 = 2 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY2]
      if BarleyQuality1 = 3 and BarleyQuality2 = 2 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 3 and BarleyQuality2 = 2 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 1 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 3 and BarleyQuality2 = 1 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 3 and BarleyQuality2 = 1 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 3 and BarleyQuality2 = 1 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 0 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 0 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 0 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 3 and BarleyQuality2 = 0 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 4 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 4 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 4 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 4 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 3 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 3 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 3 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 3 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 2 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 2 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 2 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 2 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 1 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 1 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 1 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY1]
      if BarleyQuality1 = 1 and BarleyQuality2 = 1 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 0 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 0 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 0 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 1 and BarleyQuality2 = 0 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 4 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 4 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 4 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 4 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 3 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 3 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 3 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 3 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 2 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 2 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 2 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 2 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 1 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 1 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 1 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 1 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 0 and BarleyQuality3 = 4 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 0 and BarleyQuality3 = 3 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 0 and BarleyQuality3 = 1 [set BarleyYield BarleyYieldY0]
      if BarleyQuality1 = 0 and BarleyQuality2 = 0 and BarleyQuality3 = 0 [set BarleyYield BarleyYieldY0]

      if any? BarleyPlants-here
      ;if BarleyYield > 0
      [
        sprout-HarvestBarleyRecords 1                                                          ;; this is used to record if the field has harvest, if yes there is a red star, if no nothing stands here. let this [die] when new sowing start
        [
          set shape "star"
          set size 0.1
          set color red
        ]
      ]

      set LandType 1                                                                          ;; after harvest, the field becomes fellow again
      set pcolor brown                                                                        ;; set color to brown
      set IrrigationDemand 0                                                                  ;; set irrigation demand to 0 since fellow fields don't need water
      set BarleyQuality 0                                                                     ;; set quality of barley to 0 since fellow fields don't have barley
      set FallowCountDown (Year * 365 - Day)                                                  ;; set the FallowCountDown to 2 so that after this time step fallowCountDown is 1, because after this procedure the procedure fallowfields substracts 1 of the value, and then would result into the possiblity to regrow straight away
      set ReadyForBarley false                                                                ;; set readyForCrops to false since it is not straight away ready for new crops
      set ReceivedWater1 0
      set ReceivedWater2 0
      set ReceivedWater3 0
      set ReceivedWater4 0
      set ReceivedWater5 0
    ]
    set HarvestCycle (HarvestCycle - 1)                                                       ;; reduce the time till harvest by 1 day
  ]
end

to FarmersToTalBarley
  ask patches with [LandType = 3]
  [
    if pycor > 17
    [
      set TotalBarleyYieldPerFarmerPerYear ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)       ;; set the barley of the farmer to his old barley plus the total yields of his just harvested barley
      if ([FallowCountDown] of patch (pxcor - 1) pycor) = 2 and ([FallowCountDown] of patch (pxcor - 1) (pycor + 1)) = 2 and ([FallowCountDown] of patch pxcor (pycor + 1)) = 2 and ([FallowCountDown] of patch (pxcor - 1) (pycor - 1)) = 2 and ([FallowCountDown] of patch (pxcor - 1) pycor) = 2
      [
        set TotalBarleyPerFarmer (TotalBarleyPerFarmer + TotalBarleyYieldPerFarmerPerYear)
      ]

    ]
    if pycor < 17
    [
      if pycor > 14                                                                             ;; the primary canal
      [
        set TotalBarleyYieldPerFarmerPerYear ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)       ;; set the barley of the farmer to his old barley plus the total yields of his just harvested barley
        if ([FallowCountDown] of patch (pxcor - 1) pycor) = 2 and ([FallowCountDown] of patch (pxcor - 1) (pycor - 1)) = 2 and ([FallowCountDown] of patch pxcor (pycor - 1)) = 2 and ([FallowCountDown] of patch (pxcor + 1) (pycor - 1)) = 2 and ([FallowCountDown] of patch (pxcor + 1) pycor) = 2
        [
          set TotalBarleyPerFarmer (TotalBarleyPerFarmer + TotalBarleyYieldPerFarmerPerYear)
        ]
      ]
      if pycor < 15                                                                             ;; the secondary canal
      [
        if pxcor < 38                                                                           ;; the left side of the secondary canal
        [
          set TotalBarleyYieldPerFarmerPerYear ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))       ;; set the barley of the farmer to his old barley plus the total yields of his just harvested barley
          if ([FallowCountDown] of patch pxcor (pycor + 1)) = 2 and ([FallowCountDown] of patch (pxcor - 1) (pycor + 1)) = 2 and ([FallowCountDown] of patch (pxcor - 1) pycor) = 2 and ([FallowCountDown] of patch (pxcor - 1) (pycor - 1)) = 2 and ([FallowCountDown] of patch pxcor (pycor - 1)) = 2
          [
            set TotalBarleyPerFarmer (TotalBarleyPerFarmer + TotalBarleyYieldPerFarmerPerYear)
          ]
        ]
        if pxcor > 38                                                                           ;; the right side of the secondary canan
        [
          set TotalBarleyYieldPerFarmerPerYear ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))       ;; set the barley of the farmer to his old barley plus the total yields of his just harvested barley
          if ([FallowCountDown] of patch pxcor (pycor + 1)) = 2 and ([FallowCountDown] of patch (pxcor + 1) (pycor + 1)) = 2 and ([FallowCountDown] of patch (pxcor + 1) pycor) = 2 and ([FallowCountDown] of patch (pxcor + 1) (pycor - 1)) = 2 and ([FallowCountDown] of patch pxcor (pycor - 1)) = 2
          [
            set TotalBarleyPerFarmer (TotalBarleyPerFarmer + TotalBarleyYieldPerFarmerPerYear)
          ]
        ]
      ]
    ]
  ]

  ask patches with [LandType = 1]                                                                          ;; ask fallow fields
  [
    if FallowCountDown = 2
    [
      ask patches with [LandType = 3]
      [
        set TotalBarleyPerFarmer (TotalBarleyPerFarmer + TotalBarleyYieldPerFarmerPerYear)
      ]
    ]
  ]
end

to FarmersHarvestSituationPerYear                                                                                     ;; use to count the number of harvested fields for each farmer
  ask patches with [LandType = 3]                                                                                     ;; ask storage patch
  [
    if day = 365 * Year - 2
    [
;;the primary canal
      if pxcor = 28
      [
        set NumberofHarvestFieldsF1 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF1 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 30
      [
        set NumberofHarvestFieldsF2 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF2 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 32
      [
        set NumberofHarvestFieldsF3 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF3 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 34
      [
        set NumberofHarvestFieldsF4 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF4 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 36
      [
        set NumberofHarvestFieldsF5 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF5 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 41
      [
        set NumberofHarvestFieldsF6 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF6 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 43
      [
        set NumberofHarvestFieldsF7 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF7 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 45
      [
        set NumberofHarvestFieldsF8 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF8 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 47
      [
        set NumberofHarvestFieldsF9 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF9 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 49
      [
        set NumberofHarvestFieldsF10 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF10 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
;;the secondary canal
      if pycor = 13
      [
        set NumberofHarvestFieldsF11 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF11 ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))
      ]
      if pycor = 11
      [
        set NumberofHarvestFieldsF12 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF12 ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))
      ]
      if pycor = 9
      [
        set NumberofHarvestFieldsF13 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF13 ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))
      ]
      if pycor = 7
      [
        set NumberofHarvestFieldsF14 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF14 ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))
      ]
      if pycor = 5
      [
        set NumberofHarvestFieldsF15 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF15 ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))
      ]
      if pycor = 3
      [
        set NumberofHarvestFieldsF16 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF16 ([BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1))
      ]
;;the 2nd primary canal
      if pxcor = 22
      [
        set NumberofHarvestFieldsF17 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF17 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 20
      [
        set NumberofHarvestFieldsF18 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF18 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 18
      [
        set NumberofHarvestFieldsF19 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF19 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 16
      [
        set NumberofHarvestFieldsF20 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF20 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 14
      [
        set NumberofHarvestFieldsF21 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF21 ([BarleyYield] of patch (pxcor + 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor + 1) + [BarleyYield] of patch pxcor (pycor + 1) + [BarleyYield] of patch (pxcor + 1) (pycor + 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
      if pxcor = 12
      [
        set NumberofHarvestFieldsF22 (count neighbors with [BarleyYield != 0])
        set BarleyYieldPerYearF22 ([BarleyYield] of patch (pxcor - 1) pycor + [BarleyYield] of patch (pxcor - 1) (pycor - 1) + [BarleyYield] of patch pxcor (pycor - 1) + [BarleyYield] of patch (pxcor + 1) (pycor - 1) + [BarleyYield] of patch (pxcor + 1) pycor)
      ]
    ]
  ]
end

to SystemsReaction_PrimaryCanal
  set CommunicationYear Year                                                               ;; record the year when farmers comparing their harvest (poor harvest year recording)
  if any? neighbors with [pcolor = red]
  [
    ask neighbors with [pcolor = red]
    [
      set ReadyforGCDecision_PrimaryCanal true
    ]
  ]
end

to SystemsReaction_SecondaryCanal
  if any? neighbors with [pcolor = red + 2]
  [
    ask neighbors with [pcolor = red + 2]
    [
      set ReadyforGCDecision_SecondaryCanal true
    ]
  ]
end

to FallowFields
  ask patches with [LandType = 6]                                                                          ;; ask prepared fields, sky
  [
    if day = 365 * Year - 2
    [
      set LandType 1
      set pcolor brown
      set IrrigationDemand 0
    ]
  ]

  ask patches with [LandType = 1]                                                                          ;; ask fallow fields
  [
    set FallowCountDown (FallowCountDown - 1)                                                               ;; for each tick reduce the fallow count down by one day
    if FallowCountDown = 1
    [
      ask patches with [LandType = 1 or LandType = 2]                                                          ;; ask fallow and barley fields
      [
        set BarleyYield 0                                                                                      ;; reset the barley weight of the just harvested fields
        ask BarleyPlants [die]                                                                                 ;; barley harvested
        set Counter 0
      ]
    ]

    if FallowCountDown = 0
    [
      ask patches with [LandType = 3]
      [
        set Landed 0
      ]
    ]

    if FallowCountDown < 0                                                                                ;; if fallow count down is lower or equal to 0
    [
      set ReadyForBarley true                                                                              ;; set ready for barley to true which allow the BarleySowSelection procedure to be active
    ]
  ]

  ask patches with [LandType = 2]
  [
    if [FallowCountDown] of patch 27 18 = 2
    [
      set LandType 1                                                                          ;; after harvest, the field becomes fellow again
      set pcolor brown                                                                        ;; set color to brown
      set IrrigationDemand 0                                                                  ;; set irrigation demand to 0 since fellow fields don't need water
      set BarleyQuality 0                                                                     ;; set quality of barley to 0 since fellow fields don't have barley
      set FallowCountDown (Year * 365 - Day)                                                  ;; set the FallowCountDown to 2 so that after this time step fallowCountDown is 1, because after this procedure the procedure fallowfields substracts 1 of the value, and then would result into the possiblity to regrow straight away
      set ReadyForBarley false                                                                ;; set readyForCrops to false since it is not straight away ready for new crops
      set ReceivedWater1 0
      set ReceivedWater2 0
      set ReceivedWater3 0
      set ReceivedWater4 0
      set ReceivedWater5 0
      ask BarleyPlants [die]
    ]
  ]

end

to Outflow
  ask patch 25 0
  [
    ask turtles-here [die]
  ]

  ask patch 51 17
  [
    ask turtles-here [die]
  ]

  ask patch 38 6
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]

  ask patch 38 4
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]

  ask patch 38 3
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]

  ask patch 38 0
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]

  ask patch 15 17
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]

  ask patch 13 17
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]

  ask patch 12 17
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]

  ask patch 9 17
  [
    if pcolor = black
    [
      ask turtles-here [die]
    ]
  ]
end

to BarleySowSelection
  ask patches with [LandType = 1]
  [
    if ReadyForBarley = true
    [
      if pycor > 17
      [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch (pxcor + 1) pycor) = 3
        [
          if count HarvestBarleyRecords-here != 0
          [
            if AverageHarvestBarley >= 440
            [
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 1.5
              [
                set SowingChoice "ExpandOneField"
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 1.5
              [
                set SowingChoice "KeepLastSeasonChoice"
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 0.5
              [
                set SowingChoice "DecreaseOneField"                                                  ;; stop farming field1
              ]
            ]
            if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
            [
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 1.5
              [
                set SowingChoice "KeepLastSeasonChoice"
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 1.5
              [
                set SowingChoice "KeepLastSeasonChoice"
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 0.5
              [
                set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
              ]
            ]
            if AverageHarvestBarley <= 55
            [
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 1.5
              [
                set SowingChoice "DecreaseOneField"
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 1.5
              [
                set SowingChoice "DecreaseOneField"
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 0.5
              [
                set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
              ]
            ]
            if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep field1
            [
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
            ]
            if SowingChoice = "ExpandOneField"                                                             ;; keep field1, expand field2
            [
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch pxcor (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseOneField"                                                      ;; stop field1
            [
              set LandType 1
              set pcolor brown
              set IrrigationDemand 0
            ]
          ]
        ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 and field2 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
        [
          if count HarvestBarleyRecords-here != 0
          [
            if AverageHarvestBarley >= 440
            [
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; start expand field3
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
              [
                ifelse any? HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                         ;; if field1 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop farming field2
                ]
              ]
              if([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                          ;; if field1 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop farming field2
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop farming field2
                ]
              ]
            ]
            if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
            [
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                          ;; if field1 harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; sowing field1 and field2
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; stop farming field2
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                          ;; if field1 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; sowing field1 and field2
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop farming field2
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                          ;; if field1 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop farming field2
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop farming field2
                ]
              ]
            ]
            if AverageHarvestBarley <= 55
            [
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                          ;; if field1 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                 ;; stop farming field2
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                      ;; if field1 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
              [
                ifelse count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                      ;; if field1 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                   ;; stop farming field2,field1
                ]
              ]
            ]

            if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
            [                                                                                         ;; keep field2 and field1
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch pxcor (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1 and field2, then expand field3
            [
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch pxcor (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor + 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseOneField"
            [
              ask patch pxcor (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseTwoFields"
            [
              set LandType 1
              set pcolor brown
              set IrrigationDemand 0
              ask patch pxcor (pycor - 1)
              [
                set LandType 1
                set pcolor brown
                set IrrigationDemand 0
              ]
            ]
          ]
        ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, and field3 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch pxcor (pycor - 1)) = 3
        [
          if count HarvestBarleyRecords-here != 0
          [
            if AverageHarvestBarley >= 440
            [
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; expand field4
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                ]
              ]
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                ]
              ]
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop field2 and field3
                ]
              ]
            ]
            if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
            [
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; expand field4
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                ]
              ]
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                ]
              ]
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop field2 and field3
                ]
              ]
            ]
            if AverageHarvestBarley <= 55
            [
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                ]
              ]
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                ]
              ]
              if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 2.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop field2 and field3
                ]
              ]
            ]
            if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
            [                                                                                         ;; keep field2 and field1
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 1) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1 and field2, then expand field3
            [
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 1) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor + 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseOneField"
            [
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 1) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseTwoFields"
            [
              ask patch (pxcor - 1) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
          ]
        ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, and field4 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
        [
          if count HarvestBarleyRecords-here != 0
          [
            if AverageHarvestBarley >= 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) >= TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; expand field5
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                ]
              ]
            ]
            if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) >= TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; expand field5
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                ]
              ]
            ]
            if AverageHarvestBarley <= 55
            [
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) >= TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor - 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                ]
              ]
            ]

            if SowingChoice = "KeepLastSeasonChoice"
            [                                                                                         ;; keep field1, feild2, field3, and field4
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "ExpandOneField"                                                        ;; expand field5
            [                                                                                         ;; keep field4
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch pxcor (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseOneField"
            [                                                                                         ;; stop field4
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseTwoFields"
            [
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
          ]
        ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, field4, and field5 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch (pxcor - 1) pycor) = 3
        [
          if count HarvestBarleyRecords-here != 0
          [
            if AverageHarvestBarley >= 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop field4 and field5
                ]
              ]
            ]
            if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop field4 and field5
                ]
              ]
            ]
            if AverageHarvestBarley <= 55
            [
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                 ;; stop field4 and field5
                ]
              ]
            ]
            if SowingChoice = "KeepLastSeasonChoice"
            [                                                                                         ;; keep field5
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch pxcor (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 1) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseOneField"
            [                                                                                        ;; stop field5
              ask patch pxcor (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 1) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseTwoFields"
            [                                                                                        ;; stop field4 and field5
              ask patch (pxcor - 1) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
          ]
        ]
      ]
      if pycor < 17
      [
        if pycor > 14
        [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          if ([LandType] of patch (pxcor + 1) pycor) = 3
          [
            if count HarvestBarleyRecords-here != 0
            [
              if AverageHarvestBarley >= 440
              [
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 1.5
                [
                  set SowingChoice "ExpandOneField"
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 1.5
                [
                  set SowingChoice "KeepLastSeasonChoice"
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 0.5
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop farming field1
                ]
              ]
              if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
              [
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 1.5
                [
                  set SowingChoice "KeepLastSeasonChoice"
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 1.5
                [
                  set SowingChoice "KeepLastSeasonChoice"
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 0.5
                [
                  set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
                ]
              ]
              if AverageHarvestBarley <= 55
              [
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 1.5
                [
                  set SowingChoice "DecreaseOneField"
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 1.5
                [
                  set SowingChoice "DecreaseOneField"
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 0.5
                [
                  set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
                ]
              ]
              if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep field1
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              if SowingChoice = "ExpandOneField"                                                             ;; keep field1, expand field2
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
                ask patch pxcor (pycor - 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
              if SowingChoice = "DecreaseOneField"                                                      ;; stop field1
              [
                set LandType 1
                set pcolor brown
                set IrrigationDemand 0
              ]
            ]
          ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 and field2 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
          [
            if count HarvestBarleyRecords-here != 0
            [
              if AverageHarvestBarley >= 440
              [
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) >= TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 harvested in the last year
                  [
                    set SowingChoice "ExpandOneField"                                                    ;; expand field3
                  ]
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                  ]
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) < TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                          ;; if field1 harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stopfield2
                  ]
                ]
                if([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) < TotalIrrigationDemand * 1.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 harvested in the last year
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field2
                  ]
                  [
                    set SowingChoice "DecreaseTwoFields"                                                  ;; stop  field2
                  ]
                ]
              ]
              if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
              [
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) >= TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 harvested in the last year
                  [
                    set SowingChoice "ExpandOneField"                                                    ;; expand field3
                  ]
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                  ]
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) < TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                          ;; if field1 harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stopfield2
                  ]
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) < TotalIrrigationDemand * 1.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 harvested in the last year
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field2
                  ]
                  [
                    set SowingChoice "DecreaseTwoFields"                                                  ;; stop  field2
                  ]
                ]
              ]

              if AverageHarvestBarley <= 55
              [
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) >= TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                          ;; if field1 harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                 ;; stop farming field2
                  ]
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) < TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                  ]
                ]
                if ([AverageAvailableWater] of patch (pxcor + 1) (pycor + 1)) < TotalIrrigationDemand * 1.5
                [
                  ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 harvested in the last year
                  [
                    set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                  ]
                  [
                    set SowingChoice "DecreaseTwoFields"                                                   ;; stop farming field2,field1
                  ]
                ]
              ]

              if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
              [                                                                                         ;; keep field2 and field1
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
                ask patch pxcor (pycor + 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
              if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1 and field2, then expand field3
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
                ask patch pxcor (pycor + 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
                ask patch (pxcor + 1) pycor
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
              if SowingChoice = "DecreaseOneField"
              [
                ask patch pxcor (pycor + 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
              if SowingChoice = "DecreaseTwoFields"
              [
                set LandType 1
                set pcolor brown
                set IrrigationDemand 0
                ask patch pxcor (pycor + 1)
                [
                  set LandType 1
                  set pcolor brown
                  set IrrigationDemand 0
                ]
              ]
            ]
          ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, and field3 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          if ([LandType] of patch pxcor (pycor + 1)) = 3
          [
            if count HarvestBarleyRecords-here != 0
            [
              if AverageHarvestBarley >= 440
              [
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 3.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "ExpandOneField"                                                    ;; expand field4
                  ]
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                  ]
                ]
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 3.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                  ]
                ]
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                  ]
                  [
                    set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                  ]
                ]
              ]
              if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
              [
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 3.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "ExpandOneField"                                                    ;; expand field4
                  ]
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                  ]
                ]
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 3.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                  ]
                ]
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                  ]
                  [
                    set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                  ]
                ]
              ]
              if AverageHarvestBarley <= 55
              [
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 3.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                  ]
                ]
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 3.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                  ]
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                  ]
                ]
                if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 2.5
                [
                  ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 and field2harvested in the last year
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                  ]
                  [
                    set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                  ]
                ]
              ]
              if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
              [                                                                                         ;; keep field2 and field1
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
                ask patch (pxcor - 1) pycor
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
                ask patch (pxcor - 1) (pycor + 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
              if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1 and field2, then expand field3
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
                ask patch (pxcor - 1) pycor
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
                ask patch (pxcor - 1) (pycor + 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
                ask patch (pxcor + 1) pycor
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
              if SowingChoice = "DecreaseOneField"
              [
                ask patch (pxcor - 1) pycor
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
                ask patch (pxcor - 1) (pycor + 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
              if SowingChoice = "DecreaseTwoFields"
              [
                ask patch (pxcor - 1) (pycor + 1)
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
              ]
            ]
          ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, and field4 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
        [
          if count HarvestBarleyRecords-here != 0
          [
            if AverageHarvestBarley >= 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; expand field5
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                ]
              ]
            ]
            if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "ExpandOneField"                                                    ;; expand field5
                ]
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                ]
              ]
            ]
            if AverageHarvestBarley <= 55
            [
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 and field2harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                ]
              ]
            ]

            if SowingChoice = "KeepLastSeasonChoice"
            [                                                                                         ;; keep field1, feild2, field3, and field4
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "ExpandOneField"                                                        ;; expand field5
            [                                                                                         ;; keep field4
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch pxcor (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseOneField"
            [                                                                                         ;; stop field4
              ask patch (pxcor - 1) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseTwoFields"
            [
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor + 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
          ]
        ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, field4, and field5 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch (pxcor - 1) pycor) = 3
        [
          if count HarvestBarleyRecords-here != 0
          [
            if AverageHarvestBarley >= 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                   ;; stop field5
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                ]
              ]
            ]
            if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
            [
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                ]
              ]
            ]
            if AverageHarvestBarley <= 55
            [
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 5.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                ]
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
              ]
              if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 4.5
              [
                ifelse count HarvestBarleyRecords-on patch (pxcor - 2) pycor != 0 and count HarvestBarleyRecords-on patch (pxcor - 2) (pycor - 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor - 1)!= 0 and count HarvestBarleyRecords-on patch pxcor (pycor - 1) != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                [
                  set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                ]
                [
                  set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                ]
              ]
            ]
            if SowingChoice = "KeepLastSeasonChoice"
            [                                                                                         ;; keep field5
              set LandType 6
              set pcolor sky
              set IrrigationDemand Pre-IrrigationDemand
              ask patch pxcor (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 1) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseOneField"
            [                                                                                        ;; stop field5
              ask patch pxcor (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 1) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
            if SowingChoice = "DecreaseTwoFields"
            [
              ask patch (pxcor - 1) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) (pycor - 1)
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
              ask patch (pxcor - 2) pycor
              [
                set LandType 6
                set pcolor sky
                set IrrigationDemand Pre-IrrigationDemand
              ]
            ]
          ]
        ]
        ]
        if pycor < 15
        [
          if pxcor < 38                                                                             ;; the left side of the secondary canal
          [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch pxcor (pycor - 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "ExpandOneField"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 0.5
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop farming field1
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 0.5
                  [
                    set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "DecreaseOneField"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "DecreaseOneField"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 0.5
                  [
                    set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
                  ]
                ]
                if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep field1
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
                if SowingChoice = "ExpandOneField"                                                             ;; keep field1, expand field2
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"                                                      ;; stop field1
                [
                  set LandType 1
                  set pcolor brown
                  set IrrigationDemand 0
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 and field2 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch (pxcor + 1) (pycor - 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field3
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                          ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stopfield2
                    ]
                  ]
                  if([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field2
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop  field2
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field3
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                          ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stopfield2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field2
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop  field2
                    ]
                  ]
                ]

                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                          ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                 ;; stop farming field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                   ;; stop farming field2,field1
                    ]
                  ]
                ]

                if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
                [                                                                                         ;; keep field2 and field1
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1 and field2, then expand field3
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor - 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"                                                     ;; keep field1
                [
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"
                [
                  set LandType 1
                  set pcolor brown
                  set IrrigationDemand 0
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 1
                    set pcolor brown
                    set IrrigationDemand 0
                  ]
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, and field3 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch (pxcor + 1) pycor) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 and field2 harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field4
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field4
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                    ]
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1) pycor) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                    ]
                  ]
                ]
                if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
                [                                                                                         ;; keep field2 and field1
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)                                                             ;; field2
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 1)                                                            ;; field1
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1, field2, and field3, then expand field3
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor - 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"
                [
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"
                [
                  ask patch (pxcor + 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, and field4 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field5
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field5
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                    ]
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor + 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                    ]
                  ]
                ]

                if SowingChoice = "KeepLastSeasonChoice"
                [                                                                                         ;; keep field1, feild2, field3, and field4
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "ExpandOneField"                                                        ;; expand field5
                [                                                                                         ;; keep field4
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"
                [                                                                                         ;; stop field4
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"
                [
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, field4, and field5 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch pxcor (pycor + 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                    ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                    ]
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                    ]
                  ]
                ]
                if SowingChoice = "KeepLastSeasonChoice"
                [                                                                                         ;; keep field5
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"
                [                                                                                        ;; stop field5
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"                                                   ;; stop field4, field5
                [
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
              ]
            ]
          ]
          if pxcor > 38                                                                             ;; the right side of the secondary canal
          [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch pxcor (pycor - 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "ExpandOneField"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 0.5
                  [
                    set SowingChoice "DecreaseOneField"                                                  ;; stop farming field1
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "KeepLastSeasonChoice"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 0.5
                  [
                    set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "DecreaseOneField"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) >= TotalIrrigationDemand * 0.5 and ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    set SowingChoice "DecreaseOneField"
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor - 1)) < TotalIrrigationDemand * 0.5
                  [
                    set SowingChoice "DecreaseOneField"                                                   ;; stop farming field1
                  ]
                ]
                if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep field1
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                ]
                if SowingChoice = "ExpandOneField"                                                             ;; keep field1, expand field2
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"                                                      ;; stop field1
                [
                  set LandType 1
                  set pcolor brown
                  set IrrigationDemand 0
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 and field2 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field3
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                          ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stopfield2
                    ]
                  ]
                  if([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field2
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop  field2
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field3
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                          ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1 and field2
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stopfield2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field2
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop  field2
                    ]
                  ]
                ]

                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) >= TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                          ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                 ;; stop farming field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) >= TotalIrrigationDemand * 1.5 and ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) (pycor - 1)) < TotalIrrigationDemand * 1.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) pycor != 0                      ;; if field1 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                   ;; stop farming field2
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                   ;; stop farming field2,field1
                    ]
                  ]
                ]

                if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
                [                                                                                         ;; keep field2 and field1
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1 and field2, then expand field3
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor - 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"                                                     ;; keep field1
                [
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"
                [
                  set LandType 1
                  set pcolor brown
                  set IrrigationDemand 0
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 1
                    set pcolor brown
                    set IrrigationDemand 0
                  ]
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, and field3 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch (pxcor - 1) pycor) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 and field2 harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field4
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                      ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field4
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                    ]
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) >= TotalIrrigationDemand * 2.5 and ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1,field2, and field3
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1) pycor) < TotalIrrigationDemand * 2.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 1) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                       ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field3
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3
                    ]
                  ]
                ]
                if SowingChoice = "KeepLastSeasonChoice"                                                  ;; keep sowing field1 and field2
                [                                                                                         ;; keep field2 and field1
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)                                                             ;; field2
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 1)                                                             ;; field1
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "ExpandOneField"                                                        ;; keep sowing field1, field2, and field3, then expand field3
                [
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor - 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"
                [
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"
                [
                  ask patch (pxcor - 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, and field4 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field5
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "ExpandOneField"                                                    ;; expand field5
                    ]
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                    ]
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) >= TotalIrrigationDemand * 3.5 and ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field1, field2, field3, and field4
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                  ]
                  if ([AverageAvailableWater] of patch (pxcor - 1)(pycor + 1)) < TotalIrrigationDemand * 3.5
                  [
                    ifelse count HarvestBarleyRecords-on patch (pxcor - 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch pxcor (pycor + 1) != 0                     ;; if field1 and field2harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field4
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field3 and field4
                    ]
                  ]
                ]

                if SowingChoice = "KeepLastSeasonChoice"
                [                                                                                         ;; keep field1, feild2, field3, and field4
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "ExpandOneField"                                                        ;; expand field5
                [                                                                                         ;; keep field4
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"
                [                                                                                         ;; stop field4
                  ask patch pxcor (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"
                [
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor - 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
              ]
            ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1 field2, field3, field4, and field5 with barley last season;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if ([LandType] of patch pxcor (pycor + 1)) = 3
            [
              if count HarvestBarleyRecords-here != 0
              [
                if AverageHarvestBarley >= 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                    ]
                  ]
                ]
                if AverageHarvestBarley > 55 and AverageHarvestBarley < 440
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                     ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                    ]
                  ]
                ]
                if AverageHarvestBarley <= 55
                [
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) >= TotalIrrigationDemand * 4.5 and ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 5.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "KeepLastSeasonChoice"                                              ;; keep field5
                    ]
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                  ]
                  if ([AverageAvailableWater] of patch pxcor (pycor + 1)) < TotalIrrigationDemand * 4.5
                  [
                    ifelse count HarvestBarleyRecords-on patch pxcor (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 2) != 0 and count HarvestBarleyRecords-on patch (pxcor + 1) (pycor + 1)!= 0 and count HarvestBarleyRecords-on patch (pxcor + 1) pycor != 0                      ;; if field1 field2 field3 field4 and field5 harvested in the last year
                    [
                      set SowingChoice "DecreaseOneField"                                                  ;; stop field5
                    ]
                    [
                      set SowingChoice "DecreaseTwoFields"                                                  ;; stop field4 and field5
                    ]
                  ]
                ]
                if SowingChoice = "KeepLastSeasonChoice"
                [                                                                                         ;; keep field5
                  set LandType 6
                  set pcolor sky
                  set IrrigationDemand Pre-IrrigationDemand
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseOneField"
                [                                                                                        ;; stop field5
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) pycor
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
                if SowingChoice = "DecreaseTwoFields"                                                   ;; stop field4, field5
                [
                  ask patch pxcor (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 2)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                  ask patch (pxcor + 1) (pycor + 1)
                  [
                    set LandType 6
                    set pcolor sky
                    set IrrigationDemand Pre-IrrigationDemand
                  ]
                ]
              ]
            ]
          ]
        ]
      ];;;pycor < 17
    ]
  ]
end

to FieldPreparation2 ;; keep field1 and expand field2
  ask patches with [LandType = 6]                                                                        ;; ask fields that need pre irrigation
  [
    if pycor > 17
    [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
      if ([LandType] of patch (pxcor + 1) pycor) = 3                                                       ;; storage patch
      [
        set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                   ;; set currentstorage of the barley field to the currentstorage of the storage patch
        ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
        [
          set Field-IrrigationVolume1 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
        ]
        [
          set Field-IrrigationVolume1 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
        ]
        let Use-Field-IrrigationVolumes1 Field-IrrigationVolume1                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
        ask patch (pxcor + 1) pycor
        [
          set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes1)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
          ask n-of Use-Field-IrrigationVolumes1 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
        ]
        sprout-IrrigationVolumes Field-IrrigationVolume1                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
        [
          set color turquoise
          set size 0.5
          set heading 0
        ]
        if count IrrigationVolumes-here >= IrrigationDemand
        [
          set IrrigationStatus "Irrigated"
        ]
        if IrrigationStatus = "Irrigated"
        [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field2;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          ask patch pxcor (pycor + 1)
          [
            set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) (pycor - 1))
            ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
            [
              set Field-IrrigationVolume2 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
            ]
            [
              set Field-IrrigationVolume2 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
            ]
            let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
            ask patch (pxcor + 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes2 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
            sprout-IrrigationVolumes Field-IrrigationVolume2                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
;            if count IrrigationVolumes-here >= IrrigationDemand
;            [
;              set IrrigationStatus "Irrigated"
;            ]
          ]
        ]
      ]
    ]
    if pycor < 17
    [
      if pycor > 14
      [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        if ([LandType] of patch (pxcor + 1) pycor) = 3                                                       ;; storage patch
        [
          set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)                                   ;; set currentstorage of the barley field to the currentstorage of the storage patch
          ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume1 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            set Field-IrrigationVolume1 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
          ]
          let Use-Field-IrrigationVolumes1 Field-IrrigationVolume1                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
          ask patch (pxcor + 1) pycor
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes1)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of Use-Field-IrrigationVolumes1 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
          sprout-IrrigationVolumes Field-IrrigationVolume1                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
          if count IrrigationVolumes-here >= IrrigationDemand
          [
            set IrrigationStatus "Irrigated"
          ]
          if IrrigationStatus = "Irrigated"
          [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field2;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            ask patch pxcor (pycor - 1)
            [
              set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) (pycor + 1))
              ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
              [
                set Field-IrrigationVolume2 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
              ]
              [
                set Field-IrrigationVolume2 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
              ]
              let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
              ask patch (pxcor + 1) (pycor + 1)
              [
                set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                ask n-of Use-Field-IrrigationVolumes2 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
              ]
              sprout-IrrigationVolumes Field-IrrigationVolume2                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
              [
                set color turquoise
                set size 0.5
                set heading 0
              ]
            ]
          ]
        ]
      ]
      if pycor < 15                                                                                         ;; the secondary canal
      [
        if pxcor < 38                                                                                        ;; the left side of the secondary canal
        [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          if ([LandType] of patch pxcor (pycor - 1)) = 3                                                       ;; storage patch
          [
            set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                   ;; set currentstorage of the barley field to the currentstorage of the storage patch
            ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
            [
              set Field-IrrigationVolume1 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
            ]
            [
              set Field-IrrigationVolume1 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
            ]
            let Use-Field-IrrigationVolumes1 Field-IrrigationVolume1                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
            ask patch pxcor (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes1)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes1 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
            sprout-IrrigationVolumes Field-IrrigationVolume1                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
            if IrrigationStatus = "Irrigated"
            [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field2;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
              ask patch (pxcor - 1) pycor
              [
                set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) (pycor - 1))
                ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
                [
                  set Field-IrrigationVolume2 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
                ]
                [
                  set Field-IrrigationVolume2 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
                ]
                let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
                ask patch (pxcor + 1) (pycor - 1)
                [
                  set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                  ask n-of Use-Field-IrrigationVolumes2 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
                ]
                sprout-IrrigationVolumes Field-IrrigationVolume2                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
                [
                  set color turquoise
                  set size 0.5
                  set heading 0
                ]
              ]
            ]
          ]
        ]
        if pxcor > 38                                                                                        ;; the right side of the secondary canal
        [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          if ([LandType] of patch pxcor (pycor - 1)) = 3                                                       ;; storage patch
          [
            set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))                                   ;; set currentstorage of the barley field to the currentstorage of the storage patch
            ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
            [
              set Field-IrrigationVolume1 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
            ]
            [
              set Field-IrrigationVolume1 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
            ]
            let Use-Field-IrrigationVolumes1 Field-IrrigationVolume1                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
            ask patch pxcor (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes1)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes1 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
            sprout-IrrigationVolumes Field-IrrigationVolume1                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
            if IrrigationStatus = "Irrigated"
            [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;field2;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
              ask patch (pxcor + 1) pycor
              [
                set CurrentStorage ([CurrentStorage] of patch (pxcor - 1) (pycor - 1))
                ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
                [
                  set Field-IrrigationVolume2 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
                ]
                [
                  set Field-IrrigationVolume2 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
                ]
                let Use-Field-IrrigationVolumes2 Field-IrrigationVolume2                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
                ask patch (pxcor - 1) (pycor - 1)
                [
                  set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                  ask n-of Use-Field-IrrigationVolumes2 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
                ]
                sprout-IrrigationVolumes Field-IrrigationVolume2                                                           ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
                [
                  set color turquoise
                  set size 0.5
                  set heading 0
                ]
              ]
            ]
          ]
        ]
      ]
    ]
    if count IrrigationVolumes-here > 0
    [
      set Counter (count IrrigationVolumes-here)
      ifelse Counter >= IrrigationDemand                                                    ;; if the current storage exceeds the maximum storage
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]                ;; ask the extra storage volumes to die (so they go out the system)
        set ReceivedWater1 IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater1 Counter
        set plabel Counter
      ]
      show word "ReceivedWater1:" ReceivedWater1
    ]
  ]
end

to FieldPreparation2-sub
  ask patches with [LandType = 6]
  [
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;the primary canal;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    if pycor > 14
    [
      if [LandType] of patch (pxcor + 1) (pycor - 1) = 3                                                            ;; field2 - upside
      [
        if Field-IrrigationVolume2 < IrrigationDemand
        [
          if [CurrentStorage] of patch (pxcor + 1) (pycor - 1) > 0
          [
            set CurrentStorage (Field-IrrigationVolume2 + [CurrentStorage] of patch (pxcor + 1) (pycor - 1))
            ifelse CurrentStorage >= IrrigationDemand
            [
              set Field-IrrigationVolume2-sub IrrigationDemand
            ]
            [
              set Field-IrrigationVolume2-sub CurrentStorage
            ]
            let Use-Field-IrrigationVolumes2-sub (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)
            ask patch (pxcor + 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2-sub)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes2-sub StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigatio
            ]
            sprout-IrrigationVolumes (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)                                                         ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
      ]
      if [LandType] of patch (pxcor + 1) (pycor + 1) = 3                                                       ;; field2 - lowside
      [
        if Field-IrrigationVolume2 < IrrigationDemand
        [
          if [CurrentStorage] of patch (pxcor + 1) (pycor + 1) > 0
          [
            set CurrentStorage (Field-IrrigationVolume2 + [CurrentStorage] of patch (pxcor + 1) (pycor + 1))
            ifelse CurrentStorage >= IrrigationDemand
            [
              set Field-IrrigationVolume2-sub IrrigationDemand
            ]
            [
              set Field-IrrigationVolume2-sub CurrentStorage
            ]
            let Use-Field-IrrigationVolumes2-sub (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)
            ask patch (pxcor + 1) (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2-sub)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes2-sub StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigatio
            ]
            sprout-IrrigationVolumes (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)                                                         ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
      ]
    ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;the secondary canal;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    if pycor < 15
    [
      if [LandType] of patch (pxcor + 1) (pycor - 1) = 3                                                            ;; field2 - left side
      [
        if Field-IrrigationVolume2 < IrrigationDemand
        [
          if [CurrentStorage] of patch (pxcor + 1) (pycor - 1) > 0
          [
            set CurrentStorage (Field-IrrigationVolume2 + [CurrentStorage] of patch (pxcor + 1) (pycor - 1))
            ifelse CurrentStorage >= IrrigationDemand
            [
              set Field-IrrigationVolume2-sub IrrigationDemand
            ]
            [
              set Field-IrrigationVolume2-sub CurrentStorage
            ]
            let Use-Field-IrrigationVolumes2-sub (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)
            ask patch (pxcor + 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2-sub)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes2-sub StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigatio
            ]
            sprout-IrrigationVolumes (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)                                                         ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
      ]
      if [LandType] of patch (pxcor - 1) (pycor - 1) = 3                                                       ;; field2 - right side
      [
        if Field-IrrigationVolume2 < IrrigationDemand
        [
          if [CurrentStorage] of patch (pxcor - 1) (pycor - 1) > 0
          [
            set CurrentStorage (Field-IrrigationVolume2 + [CurrentStorage] of patch (pxcor - 1) (pycor - 1))
            ifelse CurrentStorage >= IrrigationDemand
            [
              set Field-IrrigationVolume2-sub IrrigationDemand
            ]
            [
              set Field-IrrigationVolume2-sub CurrentStorage
            ]
            let Use-Field-IrrigationVolumes2-sub (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)
            ask patch (pxcor - 1) (pycor - 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes2-sub)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes2-sub StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigatio
            ]
            sprout-IrrigationVolumes (Field-IrrigationVolume2-sub - Field-IrrigationVolume2)                                                         ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
      ]
    ]
  ]
end

to FieldPreparation3
  ask patches with [LandType = 6]
  [
    set IrrigationDemand Pre-IrrigationDemand
    if pycor > 17
    [
      if ([LandType] of patch pxcor (pycor - 1)) = 3
      [
        if ([IrrigationStatus] of patch (pxcor - 1) pycor)= "Irrigated"
        [
          set CurrentStorage ([CurrentStorage] of patch pxcor (pycor - 1))
          ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
          ]
          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
          ask patch pxcor (pycor - 1)
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
          sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        if count IrrigationVolumes-here >= IrrigationDemand
        [
          set IrrigationStatus "Irrigated"
        ]
      ]
    ]
    if pycor < 17
    [
      if pycor > 14                                                                                         ;; the primary canal
      [
        if ([LandType] of patch pxcor (pycor + 1)) = 3
        [
          if ([IrrigationStatus] of patch (pxcor - 1) pycor)= "Irrigated"
          [
            set CurrentStorage ([CurrentStorage] of patch pxcor (pycor + 1))
            ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
            [
              set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
            ]
            [
              set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
            ]
            let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
            ask patch pxcor (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
            sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
          ]
          if count IrrigationVolumes-here >= IrrigationDemand
          [
            set IrrigationStatus "Irrigated"
          ]
        ]
      ]
      if pycor < 15                                                                                         ;; the secondary canal
      [
        if pxcor < 38                                                                                       ;; the left side of the secondary canal
        [
          if ([LandType] of patch (pxcor + 1) pycor) = 3
          [
            if ([IrrigationStatus] of patch pxcor (pycor + 1))= "Irrigated"
            [
              set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) pycor)
              ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
              [
                set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
              ]
              [
                set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
              ]
              let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
              ask patch (pxcor + 1) pycor
              [
                set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
              ]
              sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
              [
                set color turquoise
                set size 0.5
                set heading 0
              ]
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
        if pxcor > 38                                                                                           ;; the right side of the secondary canal
        [
          if ([LandType] of patch (pxcor - 1) pycor) = 3
          [
            if ([IrrigationStatus] of patch pxcor (pycor + 1))= "Irrigated"
            [
              set CurrentStorage ([CurrentStorage] of patch (pxcor - 1) pycor)
              ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
              [
                set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
              ]
              [
                set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
              ]
              let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
              ask patch (pxcor - 1) pycor
              [
                set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
              ]
              sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
              [
                set color turquoise
                set size 0.5
                set heading 0
              ]
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
      ]
    ]
    if count IrrigationVolumes-here > 0
    [
      set Counter (count IrrigationVolumes-here)
      ifelse Counter >= IrrigationDemand                                                    ;; if the current storage exceeds the maximum storage
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]                ;; ask the extra storage volumes to die (so they go out the system)
        set ReceivedWater1 IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater1 Counter
        set plabel Counter
      ]
      show word "ReceivedWater1:" ReceivedWater1
    ]
  ]
end

to FieldPreparation4
  ask patches with [LandType = 6]
  [
    set IrrigationDemand Pre-IrrigationDemand
    if pycor > 17
    [
      if ([LandType] of patch (pxcor - 1) (pycor - 1)) = 3
      [
        if ([IrrigationStatus] of patch (pxcor - 1) pycor)= "Irrigated"
        [
          set CurrentStorage ([CurrentStorage] of patch (pxcor - 1) (pycor - 1))
          ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
          ]
          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
          ask patch (pxcor - 1) (pycor - 1)
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
          sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        if count IrrigationVolumes-here >= IrrigationDemand
        [
          set IrrigationStatus "Irrigated"
        ]
      ]
    ]
    if pycor < 17
    [
      if pycor > 14                                                                                               ;; the primary canal
      [
        if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
        [
          if ([IrrigationStatus] of patch (pxcor - 1) pycor)= "Irrigated"
          [
            set CurrentStorage ([CurrentStorage] of patch (pxcor - 1) (pycor + 1))
            ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
            [
              set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
            ]
            [
              set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
            ]
            let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
            ask patch (pxcor - 1) (pycor + 1)
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
            sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
          ]
          if count IrrigationVolumes-here >= IrrigationDemand
          [
            set IrrigationStatus "Irrigated"
          ]
        ]
      ]
      if pycor < 15                                                                                               ;; the secondary canal
      [
        if pxcor < 38                                                                                             ;; the left side of the secondary canal
        [
          if ([LandType] of patch (pxcor + 1) (pycor + 1)) = 3
          [
            if ([IrrigationStatus] of patch pxcor (pycor + 1))= "Irrigated"
            [
              set CurrentStorage ([CurrentStorage] of patch (pxcor + 1) (pycor + 1))
              ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
              [
                set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
              ]
              [
                set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
              ]
              let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
              ask patch (pxcor + 1) (pycor + 1)
              [
                set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
              ]
              sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
              [
                set color turquoise
                set size 0.5
                set heading 0
              ]
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
        if pxcor > 38                                                                                             ;; the right side of the secondary canal
        [
          if ([LandType] of patch (pxcor - 1) (pycor + 1)) = 3
          [
            if ([IrrigationStatus] of patch pxcor (pycor + 1))= "Irrigated"
            [
              set CurrentStorage ([CurrentStorage] of patch (pxcor - 1) (pycor + 1))
              ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
              [
                set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
              ]
              [
                set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
              ]
              let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
              ask patch (pxcor - 1) (pycor + 1)
              [
                set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
              ]
              sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
              [
                set color turquoise
                set size 0.5
                set heading 0
              ]
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
      ]
    ]
    if count IrrigationVolumes-here > 0
    [
      set Counter (count IrrigationVolumes-here)
      ifelse Counter >= IrrigationDemand                                                                   ;; if the current storage exceeds the maximum storage
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]                                 ;; ask the extra storage volumes to die (so they go out the system)
        set ReceivedWater1 IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater1 Counter
        set plabel Counter
      ]
      show word "ReceivedWater1:" ReceivedWater1
    ]
  ]
end

to FieldPreparation5
  ask patches with [LandType = 6]
  [
    set IrrigationDemand Pre-IrrigationDemand
    if pycor > 17
    [
      if ([LandType] of patch (pxcor - 1) pycor) = 3
      [
        if ([IrrigationStatus] of patch pxcor (pycor + 1)) = "Irrigated"
        [
          set CurrentStorage ([CurrentStorage] of patch (pxcor - 1) pycor)
          ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
          [
            set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
          ]
          [
            set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
          ]
          let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
          ask patch (pxcor - 1) pycor
          [
            set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
            ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
          ]
          sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
          [
            set color turquoise
            set size 0.5
            set heading 0
          ]
        ]
        if count IrrigationVolumes-here >= IrrigationDemand
        [
          set IrrigationStatus "Irrigated"
        ]
      ]
    ]
    if pycor < 17
    [
      if pycor > 14                                                                                                  ;; the primary canal
      [
        if ([LandType] of patch (pxcor - 1) pycor) = 3
        [
          if ([IrrigationStatus] of patch pxcor (pycor - 1)) = "Irrigated"
          [
            set CurrentStorage ([CurrentStorage] of patch (pxcor - 1) pycor)
            ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
            [
              set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
            ]
            [
              set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
            ]
            let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
            ask patch (pxcor - 1) pycor
            [
              set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
              ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
            ]
            sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
            [
              set color turquoise
              set size 0.5
              set heading 0
            ]
          ]
          if count IrrigationVolumes-here >= IrrigationDemand
          [
            set IrrigationStatus "Irrigated"
          ]
        ]
      ]
      if pycor < 15                                                                                                  ;; the secondary canal
      [
        if pxcor < 38                                                                                                ;; the left side of the secondary canal
        [
          if ([LandType] of patch pxcor (pycor + 1)) = 3
          [
            if ([IrrigationStatus] of patch (pxcor - 1) pycor) = "Irrigated"
            [
              set CurrentStorage ([CurrentStorage] of patch pxcor (pycor + 1))
              ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
              [
                set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
              ]
              [
                set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
              ]
              let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
              ask patch pxcor (pycor + 1)
              [
                set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
              ]
              sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
              [
                set color turquoise
                set size 0.5
                set heading 0
              ]
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
        if pxcor > 38                                                                                                ;; the right side of the secondary canal
        [
          if ([LandType] of patch pxcor (pycor + 1)) = 3
          [
            if ([IrrigationStatus] of patch (pxcor + 1) pycor) = "Irrigated"
            [
              set CurrentStorage ([CurrentStorage] of patch pxcor (pycor + 1))
              ifelse CurrentStorage >= IrrigationDemand                                                          ;; if there is more or equal storage than the irrigation demand
              [
                set Field-IrrigationVolume3 IrrigationDemand                                                             ;; set the amount of water that needs to be supplied by irrigation in the fields to the irrigation demand of the field
              ]
              [
                set Field-IrrigationVolume3 CurrentStorage                                                               ;; if there is not sufficient storage to provide the entire irrigation demand, set the irrigation volume to currentstorage of the storage patch
              ]
              let Use-Field-IrrigationVolumes3 Field-IrrigationVolume3                                                    ;; local variable that allows the irrigation water in the storage patch to be reduced according to the amount of water used for irrigation of the barley at the field
              ask patch pxcor (pycor + 1)
              [
                set CurrentStorage (CurrentStorage - Use-Field-IrrigationVolumes3)                                     ;; update the currentstorage 0n the storage patch to a lower amount because water used for irrigation
                ask n-of Use-Field-IrrigationVolumes3 StorageVolumes-here [die]                                        ;; ask the storage volumes on the storage patch to die, the amount is equal to the amount used for irrigation
              ]
              sprout-IrrigationVolumes Field-IrrigationVolume3                                                          ;; create irrigation volumes, the amount is equal to the remaining irrigation demand
              [
                set color turquoise
                set size 0.5
                set heading 0
              ]
            ]
            if count IrrigationVolumes-here >= IrrigationDemand
            [
              set IrrigationStatus "Irrigated"
            ]
          ]
        ]
      ]
    ]
    if count IrrigationVolumes-here > 0
    [
      set Counter (count IrrigationVolumes-here)
      ifelse Counter >= IrrigationDemand                                                                   ;; if the current storage exceeds the maximum storage
      [
        ask n-of (Counter - IrrigationDemand) IrrigationVolumes-here [die]                                 ;; ask the extra storage volumes to die (so they go out the system)
        set ReceivedWater1 IrrigationDemand
        set plabel IrrigationDemand
      ]
      [
        set ReceivedWater1 Counter
        set plabel Counter
      ]
      show word "ReceivedWater1:" ReceivedWater1
    ]
  ]
end

to SecondaryCanal_Expansion
;  file-open "InitialLayout_Expansion.txt"
;  set ExpandedLandscape file-read                                                                         ;; sets the land type according to the file

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;setup three new farmers;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patch 37 13
  [
    set LandType 3                                                          ;; setup storage patch
    set pcolor grey
    set CompareOnceAYear true                                ;; the procedure of comparing the harvest every year
    set CompareEveryTwoYearsSecondary false                  ;; the procedure of comparing the harvest every two years along the secondary canal
    set ComparisonCountDownSecondary ComparisonTime
    set F11-13WithGoodHarvestYearsProcedure_1year? False
    set F11-13WithGoodHarvestYearsProcedure_2years? False
    set F11-13WithGoodHarvestYearsProcedure_3years? False
    set F11-13WithGoodHarvestYearsProcedure_4years? False
    set F11-13WithGoodHarvestYearsProcedure_5years? False
    set F11-13WithGoodHarvestYearsProcedure_6years? False
    set F11-13CountDownExpansion_1year (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_2years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_3years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_4years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_5years (ComparisonCountDownForFarmersExpansion + 1)
  ]
  ask patch 39 11
  [
    set LandType 3                                                          ;; setup storage patch
    set pcolor grey
    set CompareOnceAYear true                                ;; the procedure of comparing the harvest every year
    set CompareEveryTwoYearsSecondary false                  ;; the procedure of comparing the harvest every two years along the secondary canal
    set ComparisonCountDownSecondary ComparisonTime
    set F11-13WithGoodHarvestYearsProcedure_1year? False
    set F11-13WithGoodHarvestYearsProcedure_2years? False
    set F11-13WithGoodHarvestYearsProcedure_3years? False
    set F11-13WithGoodHarvestYearsProcedure_4years? False
    set F11-13WithGoodHarvestYearsProcedure_5years? False
    set F11-13WithGoodHarvestYearsProcedure_6years? False
    set F11-13CountDownExpansion_1year (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_2years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_3years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_4years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_5years (ComparisonCountDownForFarmersExpansion + 1)
  ]
  ask patch 37 9
  [
    set LandType 3                                                          ;; setup storage patch
    set pcolor grey
    set CompareOnceAYear true                                ;; the procedure of comparing the harvest every year
    set CompareEveryTwoYearsSecondary false                  ;; the procedure of comparing the harvest every two years along the secondary canal
    set ComparisonCountDownSecondary ComparisonTime
    set F11-13WithGoodHarvestYearsProcedure_1year? False
    set F11-13WithGoodHarvestYearsProcedure_2years? False
    set F11-13WithGoodHarvestYearsProcedure_3years? False
    set F11-13WithGoodHarvestYearsProcedure_4years? False
    set F11-13WithGoodHarvestYearsProcedure_5years? False
    set F11-13WithGoodHarvestYearsProcedure_6years? False
    set F11-13CountDownExpansion_1year (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_2years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_3years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_4years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_5years (ComparisonCountDownForFarmersExpansion + 1)
  ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;setup secondary canal;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patch 38 16
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 15
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 14
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 13
  [
    set LandType  7                                                         ;; setup secondary gate patch, color is different from the primary canal, only for coding
    set pcolor red + 2
    set ReadyforGCDecision_SecondaryCanal false
  ]
  ask patch 38 12
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 11
  [
    set LandType  7                                                        ;; setup secondary gate patch, color is different from the primary canal, only for coding
    set pcolor red + 2
    set ReadyforGCDecision_SecondaryCanal false
  ]
  ask patch 38 10
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 9
  [
    set LandType  7                                                        ;; setup secondary gate patch, color is different from the primary canal, only for coding
    set pcolor red + 2
    set ReadyforGCDecision_SecondaryCanal false
  ]
  ask patch 38 8
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 7
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 6
  [
    set LandType  5                                                        ;; setup edge of the world patch, without function
    set pcolor black
  ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;setup farmlands;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patch 37 14
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 14
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 13
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 37 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 39 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 40 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 40 11
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 40 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 39 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 37 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 9
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 8
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 37 8
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]

  if [pcolor] of patch 38 16 = blue + 2
  [
    set ContinuouslySameHarvestYear 0
  ]
end

to SecondaryCanal_Movement
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;abandon farmlands of F8-10;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Farmer8
  ask patch 44 18
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 44 19
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 45 19
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 46 19
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 46 18
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 45 18
  [
    set LandType 4
    set pcolor green + 2
    ask StorageVolumes-here [die]
  ]
;Farmer9
  ask patch 46 16
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 46 15
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 47 15
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 48 15
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 48 16
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 47 16
  [
    set LandType 4
    set pcolor green + 2
    ask StorageVolumes-here [die]
  ]
;Farmer10
  ask patch 48 18
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 48 19
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 49 19
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 50 19
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 50 18
  [
    set LandType 4
    set pcolor green + 2
    ask IrrigationVolumes-here [die]
  ]
  ask patch 49 18
  [
    set LandType 4
    set pcolor green + 2
    ask StorageVolumes-here [die]
  ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;setup three new farmers;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patch 37 13
  [
    set LandType 3                                                          ;; setup storage patch
    set pcolor grey
    set CompareOnceAYear true                                ;; the procedure of comparing the harvest every year
    set CompareEveryTwoYearsSecondary false                  ;; the procedure of comparing the harvest every two years along the secondary canal
    set ComparisonCountDownSecondary ComparisonTime
    set F11-13WithPoorHarvestYearsProcedure_1year? False
    set F11-13WithPoorHarvestYearsProcedure_2years? False
    set F11-13WithPoorHarvestYearsProcedure_3years? False
    set F11-13WithPoorHarvestYearsProcedure_4years? False
    set F11-13WithPoorHarvestYearsProcedure_5years? False
    set F11-13WithPoorHarvestYearsProcedure_6years? False
    set F11-13WithGoodHarvestYearsProcedure_1year? False
    set F11-13WithGoodHarvestYearsProcedure_2years? False
    set F11-13WithGoodHarvestYearsProcedure_3years? False
    set F11-13WithGoodHarvestYearsProcedure_4years? False
    set F11-13WithGoodHarvestYearsProcedure_5years? False
    set F11-13WithGoodHarvestYearsProcedure_6years? False
    set F11-13CountDownExpansion_1year (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_2years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_3years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_4years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_5years (ComparisonCountDownForFarmersExpansion + 1)
  ]
  ask patch 39 11
  [
    set LandType 3                                                          ;; setup storage patch
    set pcolor grey
    set CompareOnceAYear true                                ;; the procedure of comparing the harvest every year
    set CompareEveryTwoYearsSecondary false                  ;; the procedure of comparing the harvest every two years along the secondary canal
    set ComparisonCountDownSecondary ComparisonTime
    set F11-13WithPoorHarvestYearsProcedure_1year? False
    set F11-13WithPoorHarvestYearsProcedure_2years? False
    set F11-13WithPoorHarvestYearsProcedure_3years? False
    set F11-13WithPoorHarvestYearsProcedure_4years? False
    set F11-13WithPoorHarvestYearsProcedure_5years? False
    set F11-13WithPoorHarvestYearsProcedure_6years? False
    set F11-13WithGoodHarvestYearsProcedure_1year? False
    set F11-13WithGoodHarvestYearsProcedure_2years? False
    set F11-13WithGoodHarvestYearsProcedure_3years? False
    set F11-13WithGoodHarvestYearsProcedure_4years? False
    set F11-13WithGoodHarvestYearsProcedure_5years? False
    set F11-13WithGoodHarvestYearsProcedure_6years? False
    set F11-13CountDownExpansion_1year (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_2years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_3years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_4years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_5years (ComparisonCountDownForFarmersExpansion + 1)
  ]
  ask patch 37 9
  [
    set LandType 3                                                          ;; setup storage patch
    set pcolor grey
    set CompareOnceAYear true                                ;; the procedure of comparing the harvest every year
    set CompareEveryTwoYearsSecondary false                  ;; the procedure of comparing the harvest every two years along the secondary canal
    set ComparisonCountDownSecondary ComparisonTime
    set F11-13WithPoorHarvestYearsProcedure_1year? False
    set F11-13WithPoorHarvestYearsProcedure_2years? False
    set F11-13WithPoorHarvestYearsProcedure_3years? False
    set F11-13WithPoorHarvestYearsProcedure_4years? False
    set F11-13WithPoorHarvestYearsProcedure_5years? False
    set F11-13WithPoorHarvestYearsProcedure_6years? False
    set F11-13WithGoodHarvestYearsProcedure_1year? False
    set F11-13WithGoodHarvestYearsProcedure_2years? False
    set F11-13WithGoodHarvestYearsProcedure_3years? False
    set F11-13WithGoodHarvestYearsProcedure_4years? False
    set F11-13WithGoodHarvestYearsProcedure_5years? False
    set F11-13WithGoodHarvestYearsProcedure_6years? False
    set F11-13CountDownExpansion_1year (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_2years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_3years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_4years (ComparisonCountDownForFarmersExpansion + 1)
    set F11-13CountDownExpansion_5years (ComparisonCountDownForFarmersExpansion + 1)
  ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;setup secondary canal;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patch 38 16
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 15
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 14
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 13
  [
    set LandType  7                                                         ;; setup secondary gate patch, color is different from the primary canal, only for coding
    set pcolor red + 2
    set ReadyforGCDecision_SecondaryCanal false
  ]
  ask patch 38 12
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 11
  [
    set LandType  7                                                        ;; setup secondary gate patch, color is different from the primary canal, only for coding
    set pcolor red + 2
    set ReadyforGCDecision_SecondaryCanal false
  ]
  ask patch 38 10
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 9
  [
    set LandType  7                                                        ;; setup secondary gate patch, color is different from the primary canal, only for coding
    set pcolor red + 2
    set ReadyforGCDecision_SecondaryCanal false
  ]
  ask patch 38 8
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 7
  [
    set LandType  -3                                                        ;; setup secondary canal patch
    set pcolor blue + 2
  ]
  ask patch 38 6
  [
    set LandType  5                                                        ;; setup edge of the world patch, without function
    set pcolor black
  ]
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;setup farmlands;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patch 37 14
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 14
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 13
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 37 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 39 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 40 12
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 40 11
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 40 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 39 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 37 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 10
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 9
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 36 8
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
  ask patch 37 8
  [
    set LandType 1                                                         ;; setup farmland patch
    set pcolor brown
  ]
end

to set-label ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ask patches
  [                                                                            ;; aks all patches
    ifelse (count turtles-here) > 0                               ;; if the patch has any turtles go to first statement, if no turtles go to second statement
    [
      set plabel (count turtles-here)                             ;; if the patch has any turtles count the number of turtles and display this in plabel
      if pcolor = green
      [
        set plabel (count IrrigationVolumes-here)
      ]
      set plabel-color black
    ]
    [set plabel ""]                                               ;; if the patch has no turtles don't display a number in plabel
  ]
end
@#$#@#$#@
GRAPHICS-WINDOW
0
10
1568
649
-1
-1
30.0
1
10
1
1
1
0
0
0
1
0
51
0
20
1
1
1
ticks
30.0

BUTTON
1575
35
1647
68
NIL
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
1580
75
1643
108
NIL
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
1580
115
1643
148
NIL
go
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

MONITOR
65
655
122
700
NIL
time
17
1
11

MONITOR
5
655
62
700
day
ticks
17
1
11

SLIDER
0
705
172
738
Qin_average
Qin_average
0
5000
700.0
10
1
NIL
HORIZONTAL

SWITCH
130
660
277
693
QHeadGateLimit?
QHeadGateLimit?
0
1
-1000

SLIDER
0
740
172
773
QHeadGateMaxFixed
QHeadGateMaxFixed
0
1000
200.0
50
1
NIL
HORIZONTAL

SWITCH
285
660
402
693
QGateLimit?
QGateLimit?
0
1
-1000

SLIDER
0
775
172
808
QGateMaxFixed
QGateMaxFixed
0
410
200.0
10
1
NIL
HORIZONTAL

SLIDER
0
815
237
848
MaximunStorageOfStoragePatch
MaximunStorageOfStoragePatch
0
3000
200.0
1
1
NIL
HORIZONTAL

SLIDER
355
775
527
808
BarleyIrrigationMemory
BarleyIrrigationMemory
0
37
36.0
1
1
NIL
HORIZONTAL

SLIDER
175
740
352
773
BarleyIrrigationDemand
BarleyIrrigationDemand
0
82
82.0
1
1
NIL
HORIZONTAL

SLIDER
175
705
347
738
BarleyHarvestCycle
BarleyHarvestCycle
0
181
180.0
1
1
NIL
HORIZONTAL

SLIDER
1120
655
1292
688
BarleyYieldY6
BarleyYieldY6
0
880
880.0
10
1
NIL
HORIZONTAL

SLIDER
1120
690
1292
723
BarleyYieldY5
BarleyYieldY5
0
440
440.0
10
1
NIL
HORIZONTAL

SLIDER
1120
725
1292
758
BarleyYieldY4
BarleyYieldY4
0
220
220.0
10
1
NIL
HORIZONTAL

SLIDER
355
705
527
738
StartBarley
StartBarley
0
44
44.0
1
1
NIL
HORIZONTAL

SLIDER
1305
655
1477
688
StartBarleyF1
StartBarleyF1
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1305
690
1477
723
StartBarleyF2
StartBarleyF2
0
3
2.75
0.05
1
NIL
HORIZONTAL

SLIDER
1305
725
1477
758
StartBarleyF3
StartBarleyF3
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1305
760
1477
793
StartBarleyF4
StartBarleyF4
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1305
795
1477
828
StartBarleyF5
StartBarleyF5
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1480
655
1652
688
StartBarleyF6
StartBarleyF6
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1480
690
1652
723
StartBarleyF7
StartBarleyF7
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1480
725
1652
758
StartBarleyF8
StartBarleyF8
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1480
760
1652
793
StartBarleyF9
StartBarleyF9
0
3
3.0
0.05
1
NIL
HORIZONTAL

SLIDER
1480
795
1652
828
StartBarleyF10
StartBarleyF10
0
3
3.0
0.05
1
NIL
HORIZONTAL

INPUTBOX
220
865
372
925
DaysFromStartForBarleySowSelection
185.0
1
0
Number

SLIDER
355
810
527
843
Pre-IrrigationDemand
Pre-IrrigationDemand
0
120
82.0
1
1
NIL
HORIZONTAL

SLIDER
1120
760
1292
793
BarleyYieldY3
BarleyYieldY3
0
110
110.0
1
1
NIL
HORIZONTAL

SLIDER
1120
795
1292
828
BarleyYieldY2
BarleyYieldY2
0
55
55.0
1
1
NIL
HORIZONTAL

SLIDER
1120
830
1292
863
BarleyYieldY1
BarleyYieldY1
0
27
27.0
1
1
NIL
HORIZONTAL

SLIDER
1120
865
1292
898
BarleyYieldY0
BarleyYieldY0
0
0
0.0
0
1
NIL
HORIZONTAL

SWITCH
410
660
513
693
Seed?
Seed?
1
1
-1000

INPUTBOX
0
865
217
925
RandomSeed
290449
1
0
String

MONITOR
1585
155
1642
200
Year
floor (day / 365) + 1
17
1
11

SLIDER
355
740
527
773
TotalIrrigationDemand
TotalIrrigationDemand
0
410
410.0
10
1
NIL
HORIZONTAL

PLOT
1895
10
2130
180
Barley yield of F2
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 29 16"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 29 15"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 30 15"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 31 15"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 31 16"
"BYF2" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 30 16"

PLOT
1660
10
1895
180
Barley yield of F1
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 27 18"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 27 19"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 28 19"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 29 19"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 29 18"
"BYF1" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 28 18"
"pen-6" 1.0 0 -7500403 true "" "plot [TotalBarleyPerFarmer] of patch 28 18"

PLOT
1660
180
1895
350
Barley yield of F3
Day
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 31 18"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 31 19"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 32 19"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 33 19"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 33 18"
"BYF3" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 32 18"

PLOT
1895
180
2130
350
Barley yield of F4
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 33 16"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 33 15"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 34 15"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 35 15"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 35 16"
"BYF4" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 34 16"

PLOT
1660
350
1895
520
Barley yield of F5
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 35 18"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 35 19"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 36 19"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 37 19"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 37 18"
"BYF5" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 36 18"

PLOT
1895
350
2130
520
Barley yield of F6
Time (days)
Yields (kg/ton)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 40 18"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 40 19"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 41 19"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 42 19"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 42 18"
"BYF6" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 41 18"

PLOT
1660
520
1895
690
Barley yield F7
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 42 16"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 42 15"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 43 15"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 44 15"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 44 16"
"BYF7" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 43 16"

PLOT
1895
520
2130
690
Barley yield F8
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 44 18"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 44 19"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 45 19"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 46 19"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 45 18"
"BFY8" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 45 18"

PLOT
1660
690
1895
860
Barley yield F9
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 46 16"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 46 15"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 47 15"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 48 15"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 49 16"
"BYF9" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 47 16"

PLOT
1895
690
2130
860
Barley yield of F10
Time (days)
Yields (kg/ha)
0.0
10.0
0.0
10.0
true
true
"" ""
PENS
"Field1" 1.0 0 -2674135 true "" "plot [BarleyYield] of patch 48 18"
"Field2" 1.0 0 -955883 true "" "plot [BarleyYield] of patch 48 19"
"Field3" 1.0 0 -6459832 true "" "plot [BarleyYield] of patch 49 19"
"Field4" 1.0 0 -1184463 true "" "plot [BarleyYield] of patch 50 19"
"Field5" 1.0 0 -10899396 true "" "plot [BarleyYield] of patch 50 18"
"BYF10" 1.0 2 -16777216 true "" "plot [TotalBarleyYieldPerFarmerPerYear] of patch 49 18"

SLIDER
520
660
692
693
Qin_randomizer
Qin_randomizer
0
100
0.0
1
1
NIL
HORIZONTAL

SLIDER
760
730
932
763
CountDownF3
CountDownF3
1
20
3.0
1
1
NIL
HORIZONTAL

SLIDER
525
880
712
913
ComparisonTime
ComparisonTime
365
3650
730.0
365
1
NIL
HORIZONTAL

SLIDER
940
655
1112
688
CountDownF6
CountDownF6
1
20
4.0
1
1
NIL
HORIZONTAL

SLIDER
940
690
1112
723
CountDownF7
CountDownF7
1
20
4.0
1
1
NIL
HORIZONTAL

SLIDER
940
800
1112
833
CountDownF10
CountDownF10
1
20
4.0
1
1
NIL
HORIZONTAL

SLIDER
545
775
717
808
QGateMaxFixed3
QGateMaxFixed3
0
410
149.0
1
1
NIL
HORIZONTAL

SLIDER
545
810
717
843
CSHY
CSHY
1
10
5.0
1
1
NIL
HORIZONTAL

SLIDER
545
840
717
873
CPHY
CPHY
1
10
5.0
1
1
NIL
HORIZONTAL

SLIDER
740
845
1022
878
ComparisonCountDownForCanalExpansion
ComparisonCountDownForCanalExpansion
1
365
365.0
1
1
NIL
HORIZONTAL

SLIDER
740
885
1037
918
ComparisonCountDownForFarmersExpansion
ComparisonCountDownForFarmersExpansion
0
365
365.0
1
1
NIL
HORIZONTAL

SLIDER
740
920
962
953
CountDownForWaterAvailability
CountDownForWaterAvailability
1
365
365.0
1
1
NIL
HORIZONTAL

SLIDER
1010
945
1227
978
CountDownForHarvestMemory
CountDownForHarvestMemory
0
365
365.0
1
1
NIL
HORIZONTAL

@#$#@#$#@
## WHAT IS IT?

A model that simulates a river with 10 farmers, each having 4 fields where they can grow 3 types of crops on with different properties, investemnt costs and potential revenues.

## HOW IT WORKS

(what rules the agents use to create the overall behavior of the model)

## HOW TO USE IT

(how to use the model, including a description of each of the items in the Interface tab)

## THINGS TO NOTICE

(suggested things for the user to notice while running the model)

## THINGS TO TRY

(suggested things for the user to try to do (move sliders, switches, etc.) with the model)

## EXTENDING THE MODEL

(suggested things to add or change in the Code tab to make the model more complicated, detailed, accurate, etc.)

## NETLOGO FEATURES

(interesting or unusual features of NetLogo that the model uses, particularly in the Code tab; or where workarounds were needed for missing features)

## RELATED MODELS

(models in the NetLogo Models Library and elsewhere which are of related interest)

## CREDITS AND REFERENCES

(a reference to the model's URL on the web if it has one, as well as any other necessary credits, citations, and links)
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

farmerbroke
false
15
Polygon -2064490 true false 78 163 68 165 68 170 76 167 65 179 71 183 80 182 94 167
Polygon -6459832 true false 92 297 102 297 61 79 56 80
Polygon -16777216 true false 120 299 77 301 79 286 101 285
Polygon -16777216 true false 185 300 228 302 226 287 204 286
Polygon -2064490 true false 232 166 242 168 242 173 234 170 245 182 239 186 230 185 216 171
Circle -2064490 true false 122 22 54
Polygon -2064490 true false 139 120 169 120 169 67 140 68 139 120
Polygon -1 true true 125 179 181 180 192 133 219 171 232 168 193 74 185 74 170 74 155 89 155 134 140 74 117 75 79 165 94 168 119 133
Polygon -13345367 true false 124 179 124 74 139 74 139 119 169 119 169 74 184 74 184 179 214 284 184 299 154 224 124 299 94 284
Polygon -6459832 true false 121 42 133 33 158 30 175 38 210 29 207 21 165 17 158 6 119 9 115 27 87 40 88 49
Polygon -6459832 true false 69 294 74 294
Polygon -2064490 true false 78 163 68 165 68 170 76 167 84 170 83 170 89 168 94 167
Polygon -7500403 true false 20 46 30 88 79 77 68 35 71 74 60 36 63 76 53 38 55 75 45 40 48 75 37 43 41 80 30 44 34 80
Circle -16777216 true false 137 42 6
Circle -16777216 true false 154 40 6
Line -16777216 false 147 66 159 66
Polygon -7500403 true false 19 46 67 35 76 71 34 83 27 72

farmerrich
false
15
Polygon -2064490 true false 78 163 68 165 68 170 76 167 65 179 71 183 80 182 94 167
Polygon -6459832 true false 92 297 102 297 61 79 56 80
Polygon -16777216 true false 120 299 77 301 79 286 101 285
Polygon -16777216 true false 185 300 228 302 226 287 204 286
Polygon -2064490 true false 232 166 242 168 242 173 234 170 245 182 239 186 230 185 216 171
Circle -2064490 true false 122 22 54
Polygon -2064490 true false 139 120 169 120 169 67 140 68 139 120
Polygon -1 true true 125 179 181 180 192 133 219 171 232 168 193 74 185 74 170 74 155 89 155 134 140 74 117 75 79 165 94 168 119 133
Polygon -13345367 true false 124 179 124 74 139 74 139 119 169 119 169 74 184 74 184 179 214 284 184 299 154 224 124 299 94 284
Polygon -6459832 true false 121 42 133 33 158 30 175 38 210 29 207 21 165 17 158 6 119 9 115 27 87 40 88 49
Polygon -6459832 true false 69 294 74 294
Polygon -2064490 true false 78 163 68 165 68 170 76 167 84 170 83 170 89 168 94 167
Polygon -7500403 true false 20 46 30 88 79 77 68 35 71 74 60 36 63 76 53 38 55 75 45 40 48 75 37 43 41 80 30 44 34 80
Circle -16777216 true false 137 42 6
Circle -16777216 true false 154 40 6
Polygon -6459832 true false 195 270 210 285 255 285 270 270 270 210 240 195 225 195 195 210 195 270
Polygon -6459832 true false 225 195 210 180 255 180 240 195
Rectangle -14835848 true false 216 214 249 220
Rectangle -14835848 true false 216 214 249 220
Rectangle -14835848 true false 216 228 249 234
Rectangle -14835848 true false 216 243 249 249
Rectangle -14835848 true false 215 214 223 233
Rectangle -14835848 true false 243 229 249 249
Rectangle -14835848 true false 228 204 231 260
Rectangle -14835848 true false 234 204 237 260
Line -16777216 false 147 66 159 66
Polygon -7500403 true false 19 46 67 35 76 71 34 83 27 72

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

irrigation
false
7
Rectangle -13791810 true false 69 176 84 191
Rectangle -16777216 false false 69 176 84 192
Rectangle -13791810 true false 45 147 60 162
Polygon -14835848 true true 157 148 194 206 199 211 205 213 211 215 220 216 229 213 240 208 291 168 297 161 299 154 300 146 298 136 294 127 232 24 227 19 221 15 214 15 205 18 198 21 131 65 123 75 119 83 121 92 124 98 128 105 134 113 141 125
Polygon -14835848 true true 299 142 292 27 291 19 290 14 287 9 283 4 277 2 267 3 261 6 246 16 230 28 224 47 230 48 243 44 265 27 268 25 271 25 274 25 278 29 279 36 282 119
Polygon -14835848 true true 89 162 200 212 213 184 175 174 79 142 71 133 62 130 50 132 85 189 90 174
Polygon -14835848 true true 121 95 116 81 117 75 124 67 198 23 203 71
Polygon -14835848 true true 170 168 116 96 114 90 113 89 113 86 114 81 116 75 126 67
Polygon -14835848 true true 98 32 97 36 98 42 100 46 103 53 113 69 127 79 135 67 128 59 118 42 116 38 117 35 123 36 169 42 181 37 192 33 176 31 124 22 111 21 105 23 102 26 99 30
Rectangle -13791810 true false 49 224 64 239
Rectangle -13791810 true false 43 282 58 297
Rectangle -13791810 true false 55 198 70 213
Rectangle -13791810 true false 25 167 40 182
Rectangle -13791810 true false 30 206 45 221
Rectangle -13791810 true false 27 236 42 251
Rectangle -13791810 true false 45 254 60 269
Rectangle -13791810 true false 24 267 39 282
Rectangle -13791810 true false 3 280 18 295
Rectangle -13791810 true false 5 251 20 266
Rectangle -13791810 true false 9 221 24 236
Rectangle -13791810 true false 11 191 26 206
Rectangle -13791810 true false 45 174 60 189
Polygon -16777216 false false 174 174 115 94 114 92 113 86 114 80 116 73 113 69 106 59 100 50 97 39 97 34 99 30 102 24 109 21 115 20 167 28 178 32 202 16 213 15 223 15 227 18 230 21 233 25 261 5 267 3 271 2 277 2 281 2 286 4 288 9 289 10 292 18 299 139 299 153 297 162 241 209 232 213 225 216 218 215 205 214 180 203 91 162 91 176 87 189 50 132 60 129 72 133 81 140
Polygon -16777216 false false 243 43 282 106 279 30 276 26 268 26 263 28
Polygon -16777216 false false 129 63 165 41 121 34 117 34 116 36 116 40
Rectangle -16777216 false false 25 167 40 183
Rectangle -16777216 false false 45 174 60 190
Rectangle -16777216 false false 55 198 70 214
Rectangle -16777216 false false 30 206 45 222
Rectangle -16777216 false false 11 191 26 207
Rectangle -16777216 false false 49 224 64 240
Rectangle -16777216 false false 9 221 24 237
Rectangle -16777216 false false 27 236 42 252
Rectangle -16777216 false false 45 254 60 270
Rectangle -16777216 false false 5 251 20 267
Rectangle -16777216 false false 24 266 39 282
Rectangle -16777216 false false 43 282 58 298
Rectangle -16777216 false false 3 279 18 295
Rectangle -16777216 false false 45 147 60 163

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

newwateringcan
false
8
Rectangle -13791810 true false 69 176 84 191
Rectangle -13791810 true false 45 147 60 162
Polygon -14835848 true false 157 148 194 206 199 211 205 213 211 215 220 216 229 213 240 208 291 168 297 161 299 154 300 146 298 136 294 127 232 24 227 19 221 15 214 15 205 18 198 21 131 65 123 75 119 83 121 92 124 98 128 105 134 113 141 125
Polygon -14835848 true false 299 142 292 27 291 19 290 14 287 9 283 4 277 2 267 3 261 6 246 16 230 28 224 47 230 48 243 44 265 27 268 25 271 25 274 25 278 29 279 36 282 119
Polygon -14835848 true false 89 162 200 212 213 184 175 174 79 142 71 133 62 130 50 132 85 189 90 174
Polygon -14835848 true false 121 95 116 81 117 75 124 67 198 23 203 71
Polygon -14835848 true false 170 168 116 96 114 90 113 89 113 86 114 81 116 75 126 67
Polygon -14835848 true false 98 32 97 36 98 42 100 46 103 53 113 69 127 79 135 67 128 59 118 42 116 38 117 35 123 36 169 42 181 37 192 33 176 31 124 22 111 21 105 23 102 26 99 30
Rectangle -13791810 true false 49 224 64 239
Rectangle -13791810 true false 43 282 58 297
Rectangle -13791810 true false 55 198 70 213
Rectangle -13791810 true false 25 167 40 182
Rectangle -13791810 true false 30 206 45 221
Rectangle -13791810 true false 27 236 42 251
Rectangle -13791810 true false 45 254 60 269
Rectangle -13791810 true false 24 267 39 282
Rectangle -13791810 true false 3 280 18 295
Rectangle -13791810 true false 5 251 20 266
Rectangle -13791810 true false 9 221 24 236
Rectangle -13791810 true false 11 191 26 206
Rectangle -13791810 true false 45 174 60 189
Polygon -16777216 false false 174 174 115 94 114 92 113 86 114 80 116 73 113 69 106 59 100 50 97 39 97 34 99 30 102 24 109 21 115 20 167 28 178 32 202 16 213 15 223 15 227 18 230 21 233 25 261 5 267 3 271 2 277 2 281 2 286 4 288 9 289 10 292 18 299 139 299 153 297 162 241 209 232 213 225 216 218 215 205 214 180 203 91 162 91 176 87 189 50 132 60 129 72 133 81 140
Polygon -16777216 false false 243 43 282 106 279 30 276 26 268 26 263 28
Polygon -16777216 false false 129 63 165 41 121 34 117 34 116 36 116 40

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

person farmer
false
0
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Polygon -1 true false 60 195 90 210 114 154 120 195 180 195 187 157 210 210 240 195 195 90 165 90 150 105 150 150 135 90 105 90
Circle -7500403 true true 110 5 80
Rectangle -7500403 true true 127 79 172 94
Polygon -13345367 true false 120 90 120 180 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 180 90 172 89 165 135 135 135 127 90
Polygon -6459832 true false 116 4 113 21 71 33 71 40 109 48 117 34 144 27 180 26 188 36 224 23 222 14 178 16 167 0
Line -16777216 false 225 90 270 90
Line -16777216 false 225 15 225 90
Line -16777216 false 270 15 270 90
Line -16777216 false 247 15 247 90
Rectangle -6459832 true false 240 90 255 300

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

raincloud
false
10
Circle -1 true false 46 75 85
Circle -1 true false 84 45 95
Circle -1 true false 149 108 60
Circle -1 true false 114 99 42
Circle -1 true false 145 59 67
Circle -1 true false 194 83 67
Circle -1 true false 106 120 44
Circle -13345367 true true 114 201 48
Polygon -13345367 true true 141 172 134 191 128 200 116 215 129 225 155 222 160 216 151 198 144 184
Circle -13345367 true true 195 179 34
Polygon -13345367 true true 211 161 208 173 206 177 198 189 210 196 225 197 228 190 216 173
Circle -13345367 true true 75 181 23
Polygon -13345367 true true 88 167 83 177 79 186 89 196 96 194 96 184

river
false
0
Polygon -7500403 true true 15 150 30 135
Polygon -7500403 true true 53 117 60 105 67 99 76 93 85 90 97 90 110 93 125 100 140 107 155 113 166 117 182 122 198 124 219 124 232 122 242 117 250 112 257 105 263 99 260 115 254 127 249 137 239 147 227 155 211 159 196 161 178 160 159 154 144 146 134 141 119 133 105 125 93 122 81 120 70 123 61 128 43 143 48 129
Polygon -7500403 true true 42 185 49 173 56 167 65 161 74 158 86 158 99 161 114 168 129 175 144 181 155 185 171 190 187 192 208 192 221 190 231 185 239 180 246 173 252 167 249 183 243 195 238 205 228 215 216 223 200 227 185 229 167 228 148 222 133 214 123 209 108 201 94 193 82 190 70 188 59 191 50 196 32 211 37 197

sheep
false
15
Circle -1 true true 203 65 88
Circle -1 true true 70 65 162
Circle -1 true true 150 105 120
Polygon -7500403 true false 218 120 240 165 255 165 278 120
Circle -7500403 true false 214 72 67
Rectangle -1 true true 164 223 179 298
Polygon -1 true true 45 285 30 285 30 240 15 195 45 210
Circle -1 true true 3 83 150
Rectangle -1 true true 65 221 80 296
Polygon -1 true true 195 285 210 285 210 240 240 210 195 210
Polygon -7500403 true false 276 85 285 105 302 99 294 83
Polygon -7500403 true false 219 85 210 105 193 99 201 83

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

storage
false
0
Rectangle -11221820 true false 75 45 225 180

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wateringcan
false
8
Rectangle -13791810 true false 69 176 84 191
Rectangle -13791810 true false 45 147 60 162
Polygon -14835848 true false 157 148 194 206 199 211 205 213 211 215 220 216 229 213 240 208 291 168 297 161 299 154 300 146 298 136 294 127 232 24 227 19 221 15 214 15 205 18 198 21 131 65 123 75 119 83 121 92 124 98 128 105 134 113 141 125
Polygon -14835848 true false 299 142 292 27 291 19 290 14 287 9 283 4 277 2 267 3 261 6 246 16 230 28 224 47 230 48 243 44 265 27 268 25 271 25 274 25 278 29 279 36 282 119
Polygon -14835848 true false 89 162 200 212 213 184 175 174 79 142 71 133 62 130 50 132 85 189 90 174
Polygon -14835848 true false 121 95 116 81 117 75 124 67 198 23 203 71
Polygon -14835848 true false 170 168 116 96 114 90 113 89 113 86 114 81 116 75 126 67
Polygon -14835848 true false 98 32 97 36 98 42 100 46 103 53 113 69 127 79 135 67 128 59 118 42 116 38 117 35 123 36 169 42 181 37 192 33 176 31 124 22 111 21 105 23 102 26 99 30
Rectangle -13791810 true false 49 224 64 239
Rectangle -13791810 true false 43 282 58 297
Rectangle -13791810 true false 55 198 70 213
Rectangle -13791810 true false 25 167 40 182
Rectangle -13791810 true false 30 206 45 221
Rectangle -13791810 true false 27 236 42 251
Rectangle -13791810 true false 45 254 60 269
Rectangle -13791810 true false 24 267 39 282
Rectangle -13791810 true false 3 280 18 295
Rectangle -13791810 true false 5 251 20 266
Rectangle -13791810 true false 9 221 24 236
Rectangle -13791810 true false 11 191 26 206
Rectangle -13791810 true false 45 174 60 189

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

wolf
false
0
Polygon -16777216 true false 253 133 245 131 245 133
Polygon -7500403 true true 2 194 13 197 30 191 38 193 38 205 20 226 20 257 27 265 38 266 40 260 31 253 31 230 60 206 68 198 75 209 66 228 65 243 82 261 84 268 100 267 103 261 77 239 79 231 100 207 98 196 119 201 143 202 160 195 166 210 172 213 173 238 167 251 160 248 154 265 169 264 178 247 186 240 198 260 200 271 217 271 219 262 207 258 195 230 192 198 210 184 227 164 242 144 259 145 284 151 277 141 293 140 299 134 297 127 273 119 270 105
Polygon -7500403 true true -1 195 14 180 36 166 40 153 53 140 82 131 134 133 159 126 188 115 227 108 236 102 238 98 268 86 269 92 281 87 269 103 269 113

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270
@#$#@#$#@
NetLogo 6.3.0
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180
@#$#@#$#@
1
@#$#@#$#@
