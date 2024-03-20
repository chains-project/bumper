Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `Override` annotation, as it's not necessary, and uses the `Collections.singleton()` method to create a set containing the mutated class, which is passed to the `getClassInfo()` method. This should fix the error and allow the code to compile successfully.