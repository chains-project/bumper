Here is the proposed patch for the client code:
```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    boolean contains = output.contains(String.format("latest: digest: %s", original.digest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(""));
    if (!contains) {
        throw new java.lang.AssertionError("StringDoesNotContainError: " + output);
    }
}
```
In the new library version, the `StringContains` constructor no longer accepts a `boolean` parameter. Therefore, we need to change the way we check if the output contains the digest string. Instead of passing `false` as the first argument to `StringContains`, we can simply create a new `StringContains` instance with an empty string, which will always match. We then check if the output contains the digest string using the `java.lang.String.contains()` method, and throw an `AssertionError` if it does not.