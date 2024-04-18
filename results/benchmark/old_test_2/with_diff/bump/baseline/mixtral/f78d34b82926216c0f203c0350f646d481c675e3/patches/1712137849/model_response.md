Sure, to fix the error, you need to update the import statement in the client code to use the new package name. Here's the fixed code:
```java
import static tokyo.peya.lib.LearnMath.sigmoid;
```
This will import the `sigmoid` method from the new package `tokyo.peya.lib`. With this change, the client code should be able to compile and run successfully.