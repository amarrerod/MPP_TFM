MetcoPath: /home/amarrero/oplink/algorithms/team
Repetitions: 25
Name_of_experiment: MPP_TFM
NameOfExperiment: MPP_TFM
Preaction: mkdir -p experimentsResults/MPP_TFM
Algorithms: MOEA_D
Individual: MenuPlanning
Evaluations: 100000000
PopSize: 190
Neihb: 30
ProbMut: 0.05
ProbCross: 1
NumDays: 20
PrimerPlato: /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/primerosplatos.txt
SegundoPlato: /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/segundosplatos.txt
Postre: /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/postres.txt
IndividualParams: 20  /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/primerosplatos.txt /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/segundosplatos.txt /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/postres.txt

Execution:  %MetcoPath/src/skeleton/main/metcoSeq %MetcoPath/scripts/run/experimentsResults/MPP_TFM/ %MetcoPath/src/skeleton/main/ PlainText %NameOfExperiment_%Algorithms_PopSize_%PopSize_Neihb_%Neihb_days_%NumDays_%Individual_%Evaluations.%rep %Algorithms %Individual EVALUATIONS %Evaluations 10000000 0 %PopSize %Neihb %ProbMut %ProbCross 13 0 ! %NumDays %PrimerPlato %SegundoPlato %Postre $ NoOp

machinefile: experimentConfigFiles/MPP_TFM/machinefile
OutputFile: experimentsResults/MPP_TFM/%NameOfExperiment_%Algorithms_PopSize_%PopSize_Neihb_%Neihb_days_%NumDays_%Individual_%Evaluations