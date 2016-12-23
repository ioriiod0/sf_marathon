package com.sf.vrp;

import com.graphhopper.jsprit.core.problem.cost.VehicleRoutingTransportCosts;
import com.graphhopper.jsprit.core.util.Coordinate;
import com.graphhopper.jsprit.core.util.VehicleRoutingTransportCostsMatrix;

public class ManhattanCostMatrix
{
    public static VehicleRoutingTransportCosts costMatrix(int dim)
    {
	VehicleRoutingTransportCostsMatrix.Builder builder = VehicleRoutingTransportCostsMatrix
                                            		.Builder
                                            		.newInstance(true);
	for (int from = 0; from < dim*dim; from++)
	{
	    for (int to = 0; to < dim*dim; to++)
	    {
		builder.addTransportDistance(locationId(from, dim), locationId(to, dim), distance(from, to, dim));
	    }
	}
	return builder.build();
    }
    
    private static String locationId(int num, int dim)
    {
	return new Coordinate(num/dim, num%dim).toString();
    }
    
    private static int distance(int from, int to, int dim)
    {
	return Math.abs(from/dim - to/dim) + Math.abs(from%dim - to%dim);
    }
}
