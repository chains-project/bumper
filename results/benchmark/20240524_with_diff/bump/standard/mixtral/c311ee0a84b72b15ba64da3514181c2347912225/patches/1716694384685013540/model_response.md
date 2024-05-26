Here is the proposed patch for the failing client code:
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
The only change I made is in the `assertThat` statement. Instead of passing `false` as the first argument to `StringContains`, I removed it, since it is not needed and is causing the error.

Note that the new library version does not seem to have any changes related to `StringContains` constructor, so I did not make any changes related to that.