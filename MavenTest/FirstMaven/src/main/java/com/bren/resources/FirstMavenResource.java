package com.bren.resources;

import com.bren.FirstMaven.api.Saying; //import my Saying class
import com.codahale.metrics.annotation.Timed;
import java.util.Random;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import java.util.concurrent.atomic.AtomicLong;
import java.util.Optional;

@Path("/FirstMaven")
@Produces (MediaType.APPLICATION_JSON)
public class FirstMavenResource {
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ values
    /*@@@@@*/private final String template;
    /*@@@@@*/private final String defaultName;
    /*@@@@@*/private final AtomicLong counter;
   //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    public FirstMavenResource(String template, String defaultName) { //constructor
        this.template = template;
        this.defaultName = defaultName;
        this.counter = new AtomicLong();
    }

    @Path("name")
    @GET //allows this to process get http get requests
    @Timed //starts a timer
    //If the client sends a request to "/FirstMaven?name=Dougie",
    //sayHello is called with "Optional.of("Dougie")
    public Saying sayHello(/*http query parameter binding - what value is named in address bar
                            */@QueryParam("name") Optional<String> name) {
        final String value = String.format(template, name.orElse(defaultName)); //format string to be a String
                                                //will return defaultName (stranger) if there is nothing provided

        return new Saying(counter.incrementAndGet(), value);
    }

    //path built by Steven
    @Path("dice") //full path is /MyFirstMaven/dice
    @GET
    @Timed
    public Saying rollDice(@QueryParam("dice") Optional<String> name) {
        Random rand = new Random(); //setup random number generator
        int upperbound = 6; //setup upperbound for number generator

        final int randomNumber = rand.nextInt(upperbound) + 1; //generate number between 1 and 6
        final String value = String.format(template, randomNumber); //format as a String to match class format
        return new Saying(counter.incrementAndGet(), value);
    }

}
