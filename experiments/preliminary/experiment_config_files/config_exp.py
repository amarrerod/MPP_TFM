#!/usr/bin/python3.6

import argparse
from prettytable import PrettyTable

algorithm_name = "MOEA_D"
problem_name = "MenuPlanning"
mutation_prob = [0.05]
crossover_prob = [1]
population_sizes = [25, 80, 140, 190, 250]
neighbourhood_sizes = [0.4, 0.3, 0.25, 0.2, 0.16]
evaluations = 100000000
number_of_days = 20
seed = 13
output_dir = "experimentsResults/MPP_TFM"
METCO_PATH = "/home/amarrero/oplink/algorithms/team"
preaction= f"Preaction: mkdir -p {output_dir}\n"
primer_plato = "PrimerPlato: /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/primerosplatos.txt\n"
segundo_plato = "SegundoPlato: /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/segundosplatos.txt\n"
postre = "Postre: /home/amarrero/oplink/algorithms/team/src/plugins/problems/MenuPlanning/databaseMenus/postres.txt\n"
EXTENSION =  ".sexp"

def configure_experiment(name, reps):
    result_table = PrettyTable()
    result_table.title = f"Experiment {name} configuration"
    result_table.field_names = ["Configuration's name", "Population size", "Portion", "Neighbourhood size", "Crossover Probability", "Mutation Probability"]
    result_table.align["Portion"] = "r"
    result_table.align["Neighbourhood size"] = "r"
    diff_experiments = 0
    for pop_size in population_sizes:
        for neighb_size in neighbourhood_sizes:
            for crossover in crossover_prob:
                for mutation in mutation_prob:
                    for i in range(1):
                        size = round(pop_size * neighb_size)
                        m = str(mutation).replace(".", "_")
                        config_name = f"{name}_{algorithm_name}_p{pop_size}_n{size}"
                        result_table.add_row([config_name, pop_size, neighb_size, size, crossover, mutation])
                        path = f"MetcoPath: {METCO_PATH}\n"
                        repetitions = f"Repetitions: 30\n"
                        experiment = f"Name_of_experiment: {name}\n"
                        experimentCamel = f"NameOfExperiment: {name}\n"
                        algorithm = f"Algorithms: {algorithm_name}\n"
                        problem = f"Individual: {problem_name}\n"
                        evals = f"Evaluations: {evaluations}\n"
                        population_size = f"PopSize: {pop_size}\n"
                        neihb = f"Neihb: {size}\n"
                        prob_mut = f"ProbMut: {mutation}\n"
                        prob_cross = f"ProbCross: {crossover}\n"
                        num_days = f"NumDays: {number_of_days}\n"
                        individual_params = f"IndividualParams: {number_of_days} {primer_plato} {segundo_plato} {postre}"
                        execution = f"Execution:  %MetcoPath/src/skeleton/main/metcoSeq %MetcoPath/scripts/run/{output_dir}/ " \
                        "%MetcoPath/src/skeleton/main/ PlainText " \
                        "%NameOfExperiment_%Algorithms_PopSize_%PopSize_Neihb_%Neihb_days_%NumDays_%Individual_%Evaluations.%rep " \
                        "%Algorithms %Individual EVALUATIONS %Evaluations 10000000 0 %PopSize %Neihb %ProbMut %ProbCross 13 0 ! " \
                        "%NumDays %PrimerPlato %SegundoPlato %Postre $ NoOp\n\n"
                        machine_file = f"machinefile: experimentConfigFiles/MPP_TFM/machinefile\n"
                        output_file = f"OutputFile: {output_dir}/%NameOfExperiment_%Algorithms_PopSize_%PopSize_Neihb_%Neihb_days_%NumDays_%Individual_%Individiual_%Evaluations"

                        diff_experiments += 1
                        with open(f"{config_name}{EXTENSION}", "w") as output:
                            output.write(path)
                            output.write(repetitions)
                            output.write(experiment)
                            output.write(experimentCamel)
                            output.write(preaction)
                            output.write(algorithm)
                            output.write(problem)
                            output.write(evals)
                            output.write(population_size)
                            output.write(neihb)
                            output.write(prob_mut)
                            output.write(prob_cross)
                            output.write(num_days)
                            output.write(primer_plato)
                            output.write(segundo_plato)
                            output.write(postre)
                            output.write(individual_params)
                            output.write("\n")
                            output.write(execution)
                            output.write(machine_file)
                            output.write(output_file)

    print(f"You have {diff_experiments} different experiments and every configuration will be repeated 30 times: {diff_experiments * 1} independent executions")
    print(result_table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Configuring MMP Experiments")
    parser.add_argument("name", help="Name of the experiment")
    parser.add_argument("repetitions", help="Repetitions for each configuration")
    args = parser.parse_args()
    name = args.name
    reps = int(args.repetitions)
    configure_experiment(name, reps)
