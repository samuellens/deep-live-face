#!/usr/bin/env python3
"""
DeepFaceLive - Real-time face swapping application.

This module provides the main entry point for the DeepFaceLive application,
including command-line interface for running the app, training models, and
development utilities.
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Optional

from xlib import appargs as lib_appargs
from xlib import os as lib_os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Application version
__version__ = "1.0.0"


class FixPathAction(argparse.Action):
    """Custom argparse action to normalize and expand file paths."""
    
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str,
        option_string: Optional[str] = None
    ) -> None:
        """Convert relative paths to absolute and expand user home directory."""
        if values is None:
            setattr(namespace, self.dest, None)
            return
        normalized_path = os.path.abspath(os.path.expanduser(values))
        setattr(namespace, self.dest, normalized_path)


def validate_path(path: Path, must_exist: bool = False, create_if_missing: bool = False) -> bool:
    """
    Validate a file or directory path.
    
    Args:
        path: The path to validate.
        must_exist: If True, the path must already exist.
        create_if_missing: If True, create the directory if it doesn't exist.
    
    Returns:
        True if the path is valid, False otherwise.
    """
    if must_exist and not path.exists():
        logger.error(f"Path does not exist: {path}")
        return False
    
    if create_if_missing and not path.exists():
        try:
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {path}")
        except OSError as e:
            logger.error(f"Failed to create directory {path}: {e}")
            return False
    
    return True


def run_deep_face_live(args: argparse.Namespace) -> int:
    """
    Run the DeepFaceLive application.
    
    Args:
        args: Parsed command-line arguments.
    
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    try:
        userdata_path = Path(args.userdata_dir) if args.userdata_dir else None
        
        if userdata_path and not validate_path(userdata_path, create_if_missing=True):
            return 1
        
        lib_appargs.set_arg_bool('NO_CUDA', args.no_cuda)
        
        if args.no_cuda:
            logger.info("CUDA disabled by user request.")
        
        logger.info("Starting DeepFaceLive...")
        
        from apps.DeepFaceLive.DeepFaceLiveApp import DeepFaceLiveApp
        DeepFaceLiveApp(userdata_path=userdata_path).run()
        
        return 0
    except ImportError as e:
        logger.error(f"Failed to import DeepFaceLive module: {e}")
        return 1
    except Exception as e:
        logger.error(f"Error running DeepFaceLive: {e}")
        return 1


def run_split_large_files(args: argparse.Namespace) -> int:
    """
    Split large files for easier distribution.
    
    Args:
        args: Parsed command-line arguments.
    
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    try:
        from scripts import dev
        dev.split_large_files()
        logger.info("Successfully split large files.")
        return 0
    except Exception as e:
        logger.error(f"Error splitting files: {e}")
        return 1


def run_merge_large_files(args: argparse.Namespace) -> int:
    """
    Merge previously split large files.
    
    Args:
        args: Parsed command-line arguments.
    
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    try:
        from scripts import dev
        dev.merge_large_files(delete_parts=args.delete_parts)
        logger.info("Successfully merged large files.")
        return 0
    except Exception as e:
        logger.error(f"Error merging files: {e}")
        return 1


def run_extract_face_synthetics(args: argparse.Namespace) -> int:
    """
    Extract faces from FaceSynthetics dataset.
    
    Args:
        args: Parsed command-line arguments.
    
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    try:
        inputdir_path = Path(args.input_dir)
        faceset_path = Path(args.faceset_path)
        
        if not validate_path(inputdir_path, must_exist=True):
            return 1
        
        from scripts import dev
        dev.extract_FaceSynthetics(inputdir_path, faceset_path)
        logger.info(f"Successfully extracted faces to {faceset_path}")
        return 0
    except Exception as e:
        logger.error(f"Error extracting FaceSynthetics: {e}")
        return 1


def train_face_aligner(args: argparse.Namespace) -> int:
    """
    Train the FaceAligner neural network.
    
    Args:
        args: Parsed command-line arguments.
    
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    try:
        workspace_path = Path(args.workspace_dir)
        faceset_path = Path(args.faceset_path)
        
        if not validate_path(workspace_path, create_if_missing=True):
            return 1
        
        if not validate_path(faceset_path, must_exist=True):
            return 1
        
        lib_os.set_process_priority(lib_os.ProcessPriority.IDLE)
        logger.info("Set process priority to IDLE for background training.")
        
        from apps.trainers.FaceAligner.FaceAlignerTrainerApp import FaceAlignerTrainerApp
        FaceAlignerTrainerApp(
            workspace_path=workspace_path,
            faceset_path=faceset_path
        )
        return 0
    except Exception as e:
        logger.error(f"Error training FaceAligner: {e}")
        return 1


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.
    
    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="DeepFaceLive",
        description="Real-time face swapping application using deep learning.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s run DeepFaceLive
  %(prog)s run DeepFaceLive --userdata-dir ~/deepface_data
  %(prog)s run DeepFaceLive --no-cuda
  %(prog)s train FaceAligner --workspace-dir ./workspace --faceset-path ./data.dfs
        """
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        default=False,
        help="Enable verbose output."
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Run command
    run_parser = subparsers.add_parser(
        "run",
        help="Run the application."
    )
    run_subparsers = run_parser.add_subparsers(dest='app', help='Application to run')
    
    # DeepFaceLive app
    dfl_parser = run_subparsers.add_parser(
        'DeepFaceLive',
        help='Run the DeepFaceLive face swapping application.'
    )
    dfl_parser.add_argument(
        '--userdata-dir',
        default=None,
        action=FixPathAction,
        help="Directory for user data and workspace files."
    )
    dfl_parser.add_argument(
        '--no-cuda',
        action="store_true",
        default=False,
        help="Disable CUDA acceleration (use CPU only)."
    )
    dfl_parser.set_defaults(func=run_deep_face_live)
    
    # Dev command
    dev_parser = subparsers.add_parser(
        "dev",
        help="Development utilities."
    )
    dev_subparsers = dev_parser.add_subparsers(dest='dev_command', help='Development commands')
    
    # Split large files
    split_parser = dev_subparsers.add_parser(
        'split_large_files',
        help='Split large files for easier distribution.'
    )
    split_parser.set_defaults(func=run_split_large_files)
    
    # Merge large files
    merge_parser = dev_subparsers.add_parser(
        'merge_large_files',
        help='Merge previously split large files.'
    )
    merge_parser.add_argument(
        '--delete-parts',
        action="store_true",
        default=False,
        help="Delete part files after merging."
    )
    merge_parser.set_defaults(func=run_merge_large_files)
    
    # Extract FaceSynthetics
    extract_parser = dev_subparsers.add_parser(
        'extract_FaceSynthetics',
        help='Extract faces from FaceSynthetics dataset.'
    )
    extract_parser.add_argument(
        '--input-dir',
        required=True,
        action=FixPathAction,
        help="FaceSynthetics dataset directory."
    )
    extract_parser.add_argument(
        '--faceset-path',
        required=True,
        action=FixPathAction,
        help="Output .dfs faceset file path."
    )
    extract_parser.set_defaults(func=run_extract_face_synthetics)
    
    # Train command
    train_parser = subparsers.add_parser(
        "train",
        help="Train neural network models."
    )
    train_subparsers = train_parser.add_subparsers(dest='model', help='Model to train')
    
    # FaceAligner trainer
    aligner_parser = train_subparsers.add_parser(
        'FaceAligner',
        help='Train the FaceAligner model.'
    )
    aligner_parser.add_argument(
        '--workspace-dir',
        required=True,
        action=FixPathAction,
        help="Training workspace directory."
    )
    aligner_parser.add_argument(
        '--faceset-path',
        required=True,
        action=FixPathAction,
        help="Path to the .dfs faceset file."
    )
    aligner_parser.set_defaults(func=train_face_aligner)
    
    return parser


def show_help(parser: argparse.ArgumentParser) -> int:
    """Display help message and exit."""
    parser.print_help()
    return 0


def main() -> int:
    """
    Main entry point for the application.
    
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    parser = create_parser()
    args = parser.parse_args()
    
    if args.verbose if hasattr(args, 'verbose') else False:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled.")
    
    if hasattr(args, 'func'):
        return args.func(args)
    else:
        return show_help(parser)


if __name__ == '__main__':
    sys.exit(main())
