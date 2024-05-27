Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(org.hamcrest.core.StringStartsWith.startsWith(java.lang.String.format("latest: digest: %s", original.digest()))));
}
```
The error message indicates that the `StringContains` constructor is expecting a single `String` argument, but is receiving a `boolean` and a `String` instead. This is because the `StringContains` constructor that takes a `Predicate` argument has been removed.

To fix this, I replaced the `StringContains` constructor with a different one that takes a `Matcher` argument. I used the `StringStartsWith` matcher to check if the output string starts with the expected substring.

Note that this patch assumes that the `cli.run` method returns a `String` that contains the digest of the `Image` object. If this is not the case, the patch may not work as expected.