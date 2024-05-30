Here is the patched method:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    boolean contains = output.contains(String.format("latest: digest: %s", original.digest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(contains ? "" : java.lang.String.format("latest: digest: %s", original.digest())));
}
```

The patch changes the way the `StringContains` matcher is created. Instead of passing a boolean value directly to the constructor, a boolean variable is created and used to conditionally create the expected value for the matcher. This is necessary because the constructor for `StringContains` changed in the new library version to only accept a single string argument.