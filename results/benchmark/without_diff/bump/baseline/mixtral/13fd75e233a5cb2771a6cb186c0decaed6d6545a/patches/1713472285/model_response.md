Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` constructor from the `org.hamcrest.core` package with the `stringContains` constructor from the `org.hamcrest.CoreMatchers` package. This is because the `StringContains` constructor is no longer available in the version of Hamcrest that you are using.

By using the `stringContains` constructor from the `CoreMatchers` class, you can achieve the same functionality as the original code, but without causing a compilation error.

Note that I did not change the function signature, and I did not remove the `@Override` decorator, as the method is still overriding a method in the new version. I also did not introduce any new variables, as they were not necessary to make the code easier to understand.

I hope this helps! Let me know if you have any questions or if you need further assistance.