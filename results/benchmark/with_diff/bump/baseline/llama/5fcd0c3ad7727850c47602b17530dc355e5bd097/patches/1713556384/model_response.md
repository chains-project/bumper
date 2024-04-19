Here's a possible patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder with the mutated class name
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass().getName());
    // Get the ClassInfo object using the ClassInfoBuilder
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData using the ClassInfo object
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
This patch creates a new `ClassInfoBuilder` with the mutated class name, then uses it to build a `ClassInfo` object. The `ClassInfo` object is then passed to the `MutationTestSummaryData` constructor, along with the other required parameters.

This patch uses the `org.pitest.classinfo.ClassInfoBuilder` class, which is a new addition in the updated library version, to create a `ClassInfo` object without relying on the removed `getClassInfo` method.