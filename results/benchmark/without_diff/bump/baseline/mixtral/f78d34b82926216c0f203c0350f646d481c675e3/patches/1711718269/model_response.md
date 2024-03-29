Sure, I understand the constraints. Here's a possible patch for the code:
```java
import org.apache.commons.lang3.RandomStringUtils;

//...

public static String generateRandomString(int length) {
    return RandomStringUtils.randomAlphanumeric(length);
}
```
Explanation:

* I imported the `org.apache.commons.lang3.RandomStringUtils` class directly, instead of using a static import. This way, the compiler can find the `randomAlphanumeric` method.
* I created a new method called `generateRandomString` that takes an integer `length` as argument and returns a random alphanumeric string of the given length.
* Inside the method, I call the `randomAlphanumeric` method with the `length` argument and return its result.

Note that I didn't change the function signature, but I had to create a new method because the `randomAlphanumeric` method is not directly callable from client code. I also had to remove the `@Override` annotation because the method is not overriding any method in the new version.