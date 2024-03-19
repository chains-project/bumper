I understand that you want a fixed version of the `imagePulled` method, and I will provide a solution that only modifies the code within the method itself. I will use the added library method `is()` from `org.hamcrest.CoreMatchers` to fix the issue.

Here's the fixed `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image)
    ).is(notNullValue());
}
```

The added `.is(notNullValue())` makes use of the `is()` method from `org.hamcrest.CoreMatchers` and the `notNullValue()` to ensure the compatibility. This should resolve the error message you received.