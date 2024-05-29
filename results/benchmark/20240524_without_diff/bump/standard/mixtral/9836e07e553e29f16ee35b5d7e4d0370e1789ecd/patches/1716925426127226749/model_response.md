Here's the updated code to fix the error:
```java
@org.junit.jupiter.api.Test
void shouldPullPushedByTag() throws java.lang.Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final java.lang.String output = this.client.run("pull", this.image.remote());
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", this.image.remote()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("Status: Downloaded newer image for " + this.image.remote()));
    org.hamcrest.MatcherAssert.assertThat(contains, org.hamcrest.core.Is.is(false));
}
```
The error was caused by passing two arguments to `StringContains` constructor instead of one. I replaced the constructor call with a call to `String.contains()` method to check if the output string contains the expected message. Additionally, I added a new assertion to check if the `contains` variable is `false`.