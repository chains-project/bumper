Here's the proposed patch:

```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image)));
}
```

The change made is to remove the `false` argument from the `StringContains` constructor. The `StringContains` constructor only takes a single argument, which is the expected substring, so passing `false` as a second argument is causing the compilation error.