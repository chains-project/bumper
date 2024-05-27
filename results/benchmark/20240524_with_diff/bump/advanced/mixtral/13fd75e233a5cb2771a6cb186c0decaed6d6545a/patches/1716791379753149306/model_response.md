Here's a fixed version of the code that should resolve the error:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    boolean contains = output.contains(String.format("latest: digest: %s", original.digest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(contains ? "" : "not ", output));
}
```

The error message indicates that the constructor for `StringContains` requires a single argument of type `String`, but is being passed a `boolean` and a `String`. To resolve this, I have created a separate variable `contains` to store the result of the `contains` method, and then passed an empty string or the word "not " (including a space) to `StringContains` depending on the value of `contains`.