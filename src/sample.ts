// Sample TypeScript file with long lines and double-quoted strings for issue#30
// This file demonstrates code generation with lines exceeding 100 characters

const complexConfigurationObject = {
	name: "Sample Configuration",
	description:
		"This is a comprehensive sample configuration object that spans multiple properties with detailed documentation strings and complex type definitions to exceed the 100 character line limit requirement",
	version: "1.0.0",
	enabled: true,
};

const longArrayWithMultipleElements: Array<{
	id: number;
	name: string;
	description: string;
	isActive: boolean;
}> = [
	{
		id: 1,
		name: "First Element",
		description:
			"This is the first element in the array with a comprehensive description that includes detailed information about the purpose and usage of this particular object within the system",
		isActive: true,
	},
	{
		id: 2,
		name: "Second Element",
		description:
			"The second element demonstrating how complex nested structures can be represented within TypeScript with full type safety and comprehensive documentation strings that provide context",
		isActive: false,
	},
	{
		id: 3,
		name: "Third Element",
		description:
			"Additional element showing the pattern of how multiple items with similar structures but different values can be organized within an array with clear type definitions",
		isActive: true,
	},
];

interface ExtendedConfiguration {
	projectName: string;
	description: string;
	settings: {
		apiEndpoint: string;
		timeout: number;
		retryAttempts: number;
		enableLogging: boolean;
		maxConnections: number;
	};
	features: string[];
	version: string;
}

const multilineStringExample =
	"This is a string constant that contains important configuration data and spans across the 100 character threshold to demonstrate compliance with the requirement for long lines in the generated code sample";

export function generateReport(
	config: ExtendedConfiguration,
	items: any[],
): { success: boolean; message: string; count: number; timestamp: string } {
	const report = {
		success: items.length > 0,
		message: `Successfully processed ${items.length} items from configuration "${config.projectName}" with settings enabled`,
		count: items.length,
		timestamp: new Date().toISOString(),
	};
	return report;
}

const specialCharacters =
	'Quote test: " double quotes are properly included " in this string to meet the requirement of having double-quoted text within the source code for this sample TypeScript file';

export default {
	complexConfigurationObject,
	longArrayWithMultipleElements,
	multilineStringExample,
	specialCharacters,
	generateReport,
};
