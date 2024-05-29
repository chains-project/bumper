Here's the proposed patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(java.lang.String.format("latest: digest: %s", original.digest())));
}
```

The issue was caused by the second argument of `StringContains` constructor, which expects a single `String` argument. However, the original code passed a `boolean` value along with a `String` value. I've updated the code to remove the `false` argument.