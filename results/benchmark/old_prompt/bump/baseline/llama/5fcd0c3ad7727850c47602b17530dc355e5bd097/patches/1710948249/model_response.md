Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `Override` annotation, as it is not necessary, and assigns the result of `coverage.getClassInfo()` to a variable named `classInfo` for easier readability.

The rest of the code remains unchanged. This patch should fix the error and allow the code to compile without issues.