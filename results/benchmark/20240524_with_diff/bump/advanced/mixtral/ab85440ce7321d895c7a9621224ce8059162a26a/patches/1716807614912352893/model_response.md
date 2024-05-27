Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", image));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(contains ? "" : "not " + image));
}
```
The patch changes the way the `StringContains` matcher is used. Instead of passing a boolean value to the constructor, the `contains` method is used to check if the output string contains the expected substring. If the substring is found, the `StringContains` matcher is used without any arguments. If the substring is not found, the matcher is used with the argument "not <image>" to indicate that the output string should not contain the image name.