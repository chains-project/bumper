Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder instance
    final ClassInfoBuilder classInfoBuilder = new ClassInfoBuilder(coverage.getClassInfo(data.getMutatedClass()));
    // Get the class info using the ClassInfoBuilder
    final ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData instance
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
Explanation:

The error is caused by the removal of the `getClassInfo(java.util.Collection<org.pitest.classinfo.ClassName>)` method from the `CoverageDatabase` class. To fix this, we create a new `ClassInfoBuilder` instance and use its `build()` method to get the `ClassInfo` object for the mutated class. We then pass this `ClassInfo` object to the `MutationTestSummaryData` constructor, along with the other required parameters.


Note that we cannot use the `getClassInfo(java.util.Collection<org.pitest.classinfo.ClassName>)` method anymore, as it has been removed in the new library version. Instead, we use the `ClassInfoBuilder` class to create a new `ClassInfo` object for the mutated class.