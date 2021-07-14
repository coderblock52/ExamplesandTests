package com.bren.FirstMaven.api;

import com.fasterxml.jackson.annotation.JsonProperty;


//class used by FirstMavenresource.java to return what is being said along with an ID
public class Saying {
	private long id;

	private String content;

	public Saying() {
		//jackson deserialization
	}

	public Saying(long id,
				  String content) {
		this.id = id;
		this.content = content;
	}

	@JsonProperty
	public long getID() {
		return id;
	}

	@JsonProperty
	public String getContent() {
		return content;
	}
}
