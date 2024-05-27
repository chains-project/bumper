Here is the proposed patch for the failing client code:
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
In the updated code, I have created a new variable `contains` to store the result of the `contains` method of the `output` string. This is because the `StringContains` constructor now only accepts a single string argument, instead of a boolean and a string.

Additionally, I have updated the argument of the `StringContains` constructor to match the new signature. The new argument is the substring that we want to check for in the `output` string.

I hope this helps to resolve the error!