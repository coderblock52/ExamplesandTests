package com.bren;

import com.bren.health.TemplateHealthCheck;
import com.bren.resources.FirstMavenResource;
import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
//import com.bren.FirstMaven.health.TemplateHealthCheck;

public class FirstMavenApplication extends Application<FirstMavenConfiguration> { //extends Application<FirstMavenConfiguration>?

    public static void main(final String[] args) throws Exception {
        new FirstMavenApplication().run(args);
    }

    @Override
    public String getName() {
        return "hello-world";
    }

    @Override
    public void initialize(final Bootstrap<FirstMavenConfiguration> bootstrap) {

    }

    @Override
    public void run(final FirstMavenConfiguration configuration,
                    final Environment environment) {
        final  FirstMavenResource resource = new FirstMavenResource(
                configuration.getTemplate(),
                configuration.getDefaultName()
        );
        final TemplateHealthCheck healthCheck =
                new TemplateHealthCheck(configuration.getTemplate());
        environment.healthChecks().register("template", healthCheck);
        environment.jersey().register(resource);
    }

}
