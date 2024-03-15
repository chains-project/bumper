It appears that the PasswordEncoder class and its methods have been removed in the new library version. Without knowing the new methods and classes provided in the library, it's impossible to provide an exact solution. However, here's a general direction you could take:

```java
@Override
protected Object createStringEncoder() {
    Object encoder = new Object(); // Replace Object with the new encoder class
    // encoder.setPasswordEncryptor(new StrongPasswordEncryptor()); // Replace with new method for setting password encryptor
    return encoder;
}
```

Please replace 'Object' with the new class name and uncomment the second line, replacing it with the new method for setting the password encryptor. 

This is a placeholder solution, and you'll need to replace the parts as per the new library's API.