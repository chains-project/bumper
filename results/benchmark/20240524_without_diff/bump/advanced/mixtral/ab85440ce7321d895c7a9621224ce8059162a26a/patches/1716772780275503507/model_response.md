Here is the updated code that should fix the error:
```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", image));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + image, contains));
}
```
In the original code, the `StringContains` constructor was being called with two arguments, but it only accepts one argument. To fix this, I created a separate variable `contains` to store the result of the `contains` method, and then passed it as the second argument to `StringContains`.

Note that I used the `contains` method of the `String` class to check if the `output` string contains the expected substring. If the `output` string contains the expected substring, `contains` will be set to `true`, otherwise it will be set to `false`. The `StringContains` matcher will then check if the `output` string contains the expected substring, and the `contains` boolean value will be ignored.