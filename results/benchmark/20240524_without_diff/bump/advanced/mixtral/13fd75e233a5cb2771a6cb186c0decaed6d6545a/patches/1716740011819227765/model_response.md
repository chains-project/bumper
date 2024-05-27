Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(java.lang.String.format("latest: digest: %s", original.digest())));
}
```
The patch removes the `false` argument from the `StringContains` constructor, which was causing the compilation error. The `StringContains` constructor only takes one argument, which is the expected substring.