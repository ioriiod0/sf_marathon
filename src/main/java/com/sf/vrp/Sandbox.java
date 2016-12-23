package com.sf.vrp;

import java.util.Collection;
import java.util.Random;

import com.graphhopper.jsprit.analysis.toolbox.Plotter;
import com.graphhopper.jsprit.analysis.toolbox.Plotter.Label;
import com.graphhopper.jsprit.core.algorithm.VehicleRoutingAlgorithm;
import com.graphhopper.jsprit.core.algorithm.box.Jsprit;
import com.graphhopper.jsprit.core.problem.Location;
import com.graphhopper.jsprit.core.problem.VehicleRoutingProblem;
import com.graphhopper.jsprit.core.problem.job.Service;
import com.graphhopper.jsprit.core.problem.solution.VehicleRoutingProblemSolution;
import com.graphhopper.jsprit.core.problem.vehicle.VehicleImpl;
import com.graphhopper.jsprit.core.problem.vehicle.VehicleType;
import com.graphhopper.jsprit.core.problem.vehicle.VehicleTypeImpl;
import com.graphhopper.jsprit.core.reporting.SolutionPrinter;
import com.graphhopper.jsprit.core.reporting.SolutionPrinter.Print;
import com.graphhopper.jsprit.core.util.Solutions;

public class Sandbox
{
    public static final int DIM = 9;
    
    public static void main(String[] args)
    {
	VehicleType vechicleType = VehicleTypeImpl.Builder
					.newInstance("SF-express")
					.addCapacityDimension(0, Integer.MAX_VALUE).build();
	
	VehicleImpl vehicle = VehicleImpl.Builder
					.newInstance("Vechicle#1")
					.setStartLocation(Location.newInstance(0, 0))
					.setEndLocation(Location.newInstance(DIM-1, DIM-1))
					.setType(vechicleType)
					.build();
	
	Collection<Service> services = RandomCargosService.generate(DIM, new Random().nextInt(DIM*DIM));
	
	VehicleRoutingProblem problem = VehicleRoutingProblem.Builder
							.newInstance()
                                            		.addVehicle(vehicle)
                                            		.addAllJobs(services)
                                            		.build();
	
	VehicleRoutingAlgorithm algorithm = Jsprit.createAlgorithm(problem);
	Collection<VehicleRoutingProblemSolution> solutions = algorithm.searchSolutions();
	VehicleRoutingProblemSolution bestSolution = Solutions.bestOf(solutions);
	SolutionPrinter.print(problem, bestSolution, Print.VERBOSE);
	Plotter plotter = new Plotter(problem, bestSolution);
        plotter.setLabel(Label.SIZE);
        plotter.plot("output/solution.png", "solution");
    }
}
