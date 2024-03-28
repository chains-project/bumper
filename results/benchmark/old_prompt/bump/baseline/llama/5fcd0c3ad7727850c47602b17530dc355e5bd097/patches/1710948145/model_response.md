Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `Override` annotation, as it's not necessary, and uses the `Collections.singleton()` method to create a collection with a single element, which is more concise and easier to read than the previous code.