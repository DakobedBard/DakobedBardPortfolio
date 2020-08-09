package org.mddarr.dakobedcustomerservice.api;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class CustomersApi {

    @RequestMapping(value = "customers")
    public String hello(){
        return "Hello";
    }

}
