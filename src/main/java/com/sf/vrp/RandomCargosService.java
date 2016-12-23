package com.sf.vrp;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.UUID;

import com.graphhopper.jsprit.core.problem.Location;
import com.graphhopper.jsprit.core.problem.job.Service;

public class RandomCargosService
{
    public static Collection<Service> generate(int dim, int amount)
    {
	Set<Point> points = new HashSet<>();
	Random generator = new Random();
	while (points.size() < amount) 
	{
	    points.add(new Point(generator.nextInt(dim), generator.nextInt(dim)));
	}
	
	Collection<Service> services = new ArrayList<>();
	for (Point point : points)
	{
	    services.add(Service.Builder.newInstance(UUID.randomUUID().toString())
		    		.setLocation(Location.newInstance(point.getX(), point.getY()))
		    		.build());
	}
	return services;
    }
}
