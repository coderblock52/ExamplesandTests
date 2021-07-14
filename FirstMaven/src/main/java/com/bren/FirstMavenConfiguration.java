package com.bren;

import io.dropwizard.Configuration;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.hibernate.validator.constraints.*;
import javax.validation.constraints.*;
import javax.validation.constraints.NotEmpty;

public class FirstMavenConfiguration extends Configuration {
	@NotEmpty //annotation to confirm this is not empty
	private String template; //string template

	@NotEmpty //annotation
	private String defaultName = "Stranger"; //default name is Stranger

	@JsonProperty //annotation to ensure a property or class behaves the way you want it to
	public void setTemplate(String template) { //setter for template
		this.template = template; //set my template to the template received
	}

	@JsonProperty
	public String getTemplate() { //getter for template
		return template; //return my template name
	}
	
	@JsonProperty
	public String getDefaultName() { //getter for default name
		return defaultName; //return the default name
	}
	
	@JsonProperty
	public void setDefaultName(String defaultName) { //setter for default name
		this.defaultName = defaultName; //set my defaultName to given defaultName
	}
}
