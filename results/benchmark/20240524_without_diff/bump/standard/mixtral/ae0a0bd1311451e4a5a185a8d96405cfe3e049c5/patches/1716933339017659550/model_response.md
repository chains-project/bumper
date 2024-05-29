Here is a fixed version of the code:
```java
@org.junit.jupiter.api.Test
void shouldPullPushedByTag() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remote());
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", this.image.remote()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + this.image.remote()));
}
```
The issue was that the `StringContains` constructor was being called with two arguments, while it only accepts one. I changed the code to first check if the output string contains the expected substring using the `String.contains` method, and then use the `StringContains` matcher with a single argument.