```java
@Test
void largeImageUploadWorks() throws Exception {
    try {
        this.buildImage();
        final String output = this.client.run("push", this.remote());
        MatcherAssert.assertThat(output, containsString("Pushed"));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```