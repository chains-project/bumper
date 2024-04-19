Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(data.getMutatedClass())),
        Collections.emptyList());
}
```
The patch adds an empty list as the fourth argument to the `MutationTestSummaryData` constructor. The `getClassInfo` method is also updated to return a list of one element, the mutated class, instead of a single `ClassInfo` object.

This patch addresses the error by providing a compatible constructor for the `MutationTestSummaryData` class that takes four arguments, which is the updated signature of the constructor in the failing code. By adding an empty list as the fourth argument, we ensure that the method can be invoked with the updated signature while still passing the same information as before.