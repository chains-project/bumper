Here is the proposed patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(java.lang.String.format("latest: digest: %s", original.digest())));
}
```

The change made is to remove the `false` argument from the `new org.hamcrest.core.StringContains` constructor, which was causing the error message. The `StringContains` constructor requires a single `String` argument, which is provided by the `String.format` method.