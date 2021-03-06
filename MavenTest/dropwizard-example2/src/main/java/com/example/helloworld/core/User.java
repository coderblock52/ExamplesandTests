package com.example.helloworld.core;

import java.security.Principal;
import java.util.Set;

public class User implements Principal {
    private final String name;

    private final Set<String> roles;

    public User(String name) {
        this.name = name;
        System.out.println("new user is: " + this.name);
        this.roles = null;
        System.out.println("new role for this user is: " + this.roles);
    }

    public User(String name, Set<String> roles) {
        this.name = name;
        System.out.println("new user is: " + this.name);
        this.roles = roles;
        System.out.println("new role for this user is: " + this.roles);
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return (int) (Math.random() * 100);
    }

    public Set<String> getRoles() {
        return roles;
    }
}
