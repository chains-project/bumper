```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    final java.lang.String expectedMessage = java.lang.String.format("Status: Downloaded newer image for %s", image);
    if (output.contains(expectedMessage)) {
        org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(false, expectedMessage));
    } else {
        org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(false, "Status: Image is up to date for " + image));
    }
}
```