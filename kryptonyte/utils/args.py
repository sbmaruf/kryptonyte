import argparse
import os


def dataset_args(parser):
    """
    These arguments are related to dataset preprocessing.
    :param parser: a parser
    :return: nothing
    """

    group = parser.add_argument_group('Dataset-description(conll-data)')
    group.add_argument('--src_lang',
                       required=True,
                       type=str,
                       help='Source language.')
    group.add_argument('--tgt_lang',
                       type=str,
                       help='Target language.')
    group.add_argument('--src_train_data',
                       required=True,
                       type=str,
                       default="data/eng.train",
                       help='Source language conll-ner train data.')
    group.add_argument('--src_val_data',
                       required=True,
                       type=str,
                       default="data/eng.testa",
                       help='Source language conll-ner validation data.')
    group.add_argument('--src_test_data',
                       type=str,
                       default="data/eng.testb",
                       help='Source language conll-ner test data.')
    group.add_argument('--tgt_train_data',
                       type=str,
                       help='Target language conll-ner train data.')
    group.add_argument('--tgt_val_data',
                       type=str,
                       help='Target language conll-ner validation data.')
    group.add_argument('--tgt_test_data',
                       type=str,
                       help='Target language conll-ner test data.')
    group = parser.add_argument_group('Embedding-matrix-description')
    group.add_argument('--emb_vocab',
                       type=str,
                       default="t-d-t",
                       help='Mentions the Vocabulary of the embedding matrix.\n'
                            't-d-t means all the data (train, dev, test) of '
                            'source language will be selected. For selecting '
                            'only train use t-None-None-None')
    group.add_argument('--emb_unk_replace',
                       type=str,
                       default="s-z",
                       help='This could be only [d/s]-[z/x/n/t]\n'
                            'd - dynamic. Singleton replacement\n'
                            's - static. all not found embeddings are <UNK>\n'
                            'z - zero initializer\n'
                            'x - xavier initializer\n'
                            'n - normal initializer\n'
                            't - truncated-normal initializer.')
    group.add_argument('--src_emb',
                       type=str,
                       default="data/es-en/wiki.es-en.tgt.mono",
                       help='Address of the source embeddings.'
                            'In case of `wrong/empty/None` arg, '
                            'value will be initialized based on `emb_vocab`.')
    group.add_argument('--tgt_emb',
                       type=str,
                       default="data/es-en/wiki.es-en.src.mono",
                       help='Address of the target embeddings.')
    group = parser.add_argument_group('Output-directory')
    group.add_argument('--save_data',
                       type=str,
                       default="",
                       help='Address of the directory where data will be saved.')
    group.add_argument('--force_run',
                       action='store_true',
                       help='If the folder already exists or no saved folder given, '
                            'it will automatically create a folder from time stamp.')


def assert_dataset_args(arg):
    if os.path.isdir(arg.save_data):
        pass


def add_md_help_argument(parser):
    """
    Create a Markdown-formatted help file.
    :param parser: a parser
    :return: nothing
    """
    parser.add_argument('-markdown',
                        action=MarkdownHelpAction,
                        help='Markdown-formatted help.')


class MarkdownHelpFormatter(argparse.HelpFormatter):
    def _format_usage(self, usage, actions, groups, prefix):
        return ""

    def format_help(self):
        print(self._prog)
        self._root_section.heading = '# Options: %s' % self._prog
        return super(MarkdownHelpFormatter, self).format_help()

    def start_section(self, heading):
        super(MarkdownHelpFormatter, self)\
            .start_section('### **%s**' % heading)

    def _format_action(self, action):
        if action.dest == "help" or action.dest == "md":
            return ""
        lines = []
        lines.append('* **-%s %s** ' % (action.dest,
                                        "[%s]" % action.default
                                        if action.default else "[]"))
        if action.help:
            help_text = self._expand_help(action)
            lines.extend(self._split_lines(help_text, 80))
        lines.extend(['', ''])
        return '\n'.join(lines)


class MarkdownHelpAction(argparse.Action):
    def __init__(self, option_strings,
                 dest=argparse.SUPPRESS, default=argparse.SUPPRESS,
                 **kwargs):
        super(MarkdownHelpAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        parser.formatter_class = MarkdownHelpFormatter
        parser.print_help()
        parser.exit()
