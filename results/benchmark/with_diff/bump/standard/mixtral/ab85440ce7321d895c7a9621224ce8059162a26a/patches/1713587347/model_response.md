Here is the fixed method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(org.hamcrest.Matchers.containsString(java.lang.String.format("Status: Downloaded newer image for %s", image)));
}
```

The issue is caused by the removal of the `containsString` method from the `StringContains` class. Instead, you should use the `containsString` method from the `Matchers` class, which has been added in the new version.