Here is the proposed patch for the client code:

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

In this patch, I removed the `false` argument from the `StringContains` constructor, as it is not needed and is causing a compilation error. The `StringContains` constructor only requires a single `String` argument, which is the expected substring. By removing the `false` argument, the code should now compile and run without errors.