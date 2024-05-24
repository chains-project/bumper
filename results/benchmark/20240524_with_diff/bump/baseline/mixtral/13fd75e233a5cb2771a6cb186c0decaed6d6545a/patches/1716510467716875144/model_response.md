Here's the updated `largeImageUploadWorks` method that should fix the error:

```java
@Test
void largeImageUploadWorks() throws Exception {
    try {
        this.buildImage();
        final String output = this.client.run("push", this.remote());
        MatcherAssert.assertThat(output, new StringContains("Pushed"));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```

The only change I made was to remove the `false` argument from the `StringContains` constructor. The error message indicates that the constructor now only accepts a single `String` argument, so I removed the boolean argument.