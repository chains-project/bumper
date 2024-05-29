Here's a fixed version of the code that should resolve the error:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(org.hamcrest.CoreMatchers.containsString(java.lang.String.format("latest: digest: %s", original.digest()))));
}
```

The issue was caused by the incorrect usage of the `StringContains` constructor. It requires a single argument of type `String`, but was being passed two arguments - a `boolean` and a `String`.

To fix the error, I replaced the `false` argument with a `containsString` method call from `org.hamcrest.CoreMatchers`. This method returns a `Matcher<String>` object that matches if the input string contains the specified substring.

The `containsString` method takes a single argument of type `String`, which is the substring to search for in the input string. In this case, it is constructed using `String.format` to include the digest of the original image.

By using `containsString` instead of the boolean value, the code now passes the expected argument type of the `StringContains` constructor.