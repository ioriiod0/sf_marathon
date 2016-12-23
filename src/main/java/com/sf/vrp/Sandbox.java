package com.sf.vrp;

import java.util.Collection;

import com.graphhopper.jsprit.core.algorithm.VehicleRoutingAlgorithm;
import com.graphhopper.jsprit.core.algorithm.box.Jsprit;
import com.graphhopper.jsprit.core.problem.Location;
import com.graphhopper.jsprit.core.problem.VehicleRoutingProblem;
import com.graphhopper.jsprit.core.problem.solution.VehicleRoutingProblemSolution;
import com.graphhopper.jsprit.core.problem.vehicle.VehicleImpl;
import com.graphhopper.jsprit.core.problem.vehicle.VehicleType;
import com.graphhopper.jsprit.core.problem.vehicle.VehicleTypeImpl;
import com.graphhopper.jsprit.core.reporting.SolutionPrinter;
import com.graphhopper.jsprit.core.util.Solutions;

public class Sandbox
{
    public static void main(String[] args)
    {
	System.out.println("Hello World!");
	VehicleType vechicleType = VehicleTypeImpl.Builder
					.newInstance("SF-express")
					.addCapacityDimension(0, 2).build();
	
	VehicleImpl vehicle = VehicleImpl.Builder
					.newInstance("Vechicle#1")
					.setStartLocation(Location.newInstance(0, 10))
					.setType(vechicleType)
					.build();
	
	VehicleRoutingProblem problem = null;
	VehicleRoutingAlgorithm algorithm = Jsprit.createAlgorithm(problem);
	Collection<VehicleRoutingProblemSolution> solutions = algorithm.searchSolutions();
	VehicleRoutingProblemSolution bestSolution = Solutions.bestOf(solutions);
	SolutionPrinter.print(problem, solution, print);
    }
}
